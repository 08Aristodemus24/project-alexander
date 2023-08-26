from flask import Flask
from flask_cors import CORS
import requests
from pathlib import Path

# ff. imports are for getting secret values from .env file
import os
from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
env_dir = Path('./').resolve()
load_dotenv(os.path.join(env_dir, '.env'))

app = Flask(__name__)

# since simple html from url http://127.0.0.1:5000 requests to
# api endpoint at http://127.0.0.1:5000/ we must set the allowed
# origins or web apps with specific urls like http://127.0.0.1:5000
# to be included otherwise it will be blocked by CORS policy
CORS(app, origins=["http://127.0.0.1:5500"])

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
