from flask import Flask, request
from flask_cors import CORS

import requests
import json

# ff. imports are for getting secret values from .env file
from pathlib import Path
import os
from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
env_dir = Path('./').parent.resolve()
load_dotenv(os.path.join(env_dir, '.env'))

app = Flask(__name__)

# since simple html from url http://127.0.0.1:5000 requests to
# api endpoint at http://127.0.0.1:5000/ we must set the allowed
# origins or web apps with specific urls like http://127.0.0.1:5000
# to be included otherwise it will be blocked by CORS policy
CORS(app, origins=["http://127.0.0.1:5500", "http://127.0.0.1:5173"])

@app.route('/', methods=['GET'])
def index():
    """
    flask app will run at http://127.0.0.1:5000 if /
    in url succeeds another string <some string> then
    app will run at http://127.0.0.1:5000/<some string>

    returns json of all github repositories using
    github access token
    """

    url = 'https://api.github.com/users/08Aristodemus24/repos'
    accept = 'application/vnd.github+json'
    auth_token = f"Bearer {os.environ['GITHUB_ACCESS_TOKEN']}"
    headers = {
        "Accept": accept,
        "Authorization": auth_token
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    # check if response returns an 'ok' (200) status 
    if response.status_code == 200:
        return data
    
    # if error occurs in request just return the key value
    # pairs of the response.json() dictionary and the status
    # code of the response object
    return dict(documentation_url=data['documentation_url'], message=data['message'], status_code=response.status_code)

@app.route('/send-mail', methods=['POST'])
def send_mail():
    """
    catches the http post request from the form in the front end
    and makes a proxy request to email.js to post the raw data
    in order to send as an email to designated email
    """
    # prints the ff: {'first_name': '<first name>', 'last_name': 
    # '<last name>', 'email_address': '<email_address>', 'country_code': 
    # '<country code>', 'mobile_num': '<mobile number>', 'message': '<message>'}
    raw_data = request.json
    print(type(raw_data))
    print(raw_data)
    
    url = 'https://api.emailjs.com/api/v1.0/email/send'
    headers = {
        'content-type': 'application/json'
    }
    data = {
        'service_id': os.environ['SERVICE_ID'],
        'template_id': os.environ['TEMPLATE_ID'],
        'user_id': os.environ['PUBLIC_KEY'],
        'accessToken': os.environ['PRIVATE_KEY'],
        'template_params': raw_data
    }

    response = requests.post(url=url, headers=headers, data=json.dumps(data))
    

    if response.status_code == 200:
        print('submission successful')
        return json.dumps(({'success': True}, 200, {'Content-Type': 'application/json'}))
    
    else:
        print('submission unsucessful')
        print(response.status_code)
        print(response.text)
        return json.dumps(({'success': False}, response.status_code, {'Content-Type': 'application/json'}))

if __name__ == "__main__":
    app.run(debug=True)