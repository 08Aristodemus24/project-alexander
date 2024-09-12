from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

import requests
from requests.exceptions import ConnectionError
from urllib3.exceptions import MaxRetryError, NameResolutionError
import json
from bs4 import BeautifulSoup
from datetime import datetime as dt

# ff. imports are for getting secret values from .env file
from pathlib import Path
import os
from dotenv import load_dotenv

# # Build paths inside the project like this: BASE_DIR / 'subdir'.
# # use this only in development
# env_dir = Path('./').resolve()
# load_dotenv(os.path.join(env_dir, '.env'))

# and this for production
load_dotenv()

# # configure location of build file and the static html template file
# app = Flask(__name__, static_url_path='/', static_folder='../client-side/dist')
app = Flask(__name__, template_folder='static')

# since simple html from url http://127.0.0.1:5000 requests to
# api endpoint at http://127.0.0.1:5000/ we must set the allowed
# origins or web apps with specific urls like http://127.0.0.1:5000
# to be included otherwise it will be blocked by CORS policy
# CORS(app, origins=["http://127.0.0.1:5500", "http://127.0.0.1:5173", "https://project-alexander.onrender.com"])
CORS(app, origins=["http://127.0.0.1:5500", "http://127.0.0.1:5173", "https://project-alexander.vercel.app"])

@app.route('/')
def index():
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(error):
    print(error)
    return 'This page does not exist', 404


@app.route('/repos', methods=['GET'])
@app.route('/repos/<int:repo_limit>', methods=['GET'])
@app.route('/repos/all', methods=['GET'])
def get_repos(repo_limit=None):
    """
    flask app will run at http://127.0.0.1:5000 if /
    in url succeeds another string <some string> then
    app will run at http://127.0.0.1:5000/<some string>

    returns json of all github repositories using
    github access token
    """

    # if no limit is provided for number 
    # of repos to fetch use default of 30
    url = "https://api.github.com/users/08Aristodemus24/repos{}".format('' if repo_limit == None else f'?per_page={repo_limit}')
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
        print(data)
        return data
    
    # if error occurs in request just return the key value
    # pairs of the response.json() dictionary and the status
    # code of the response object
    return json.dumps({'success': False}, response.status_code, {'Content-Type': 'application/json'})

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
        return json.dumps(({'success': True, 'message': 'submission successful'}, 200, {'Content-Type': 'application/text'}))
    
    else:
        print(f'submission unsucessful.\nstatus code: {response.status_code}\nmessage: {response.text}')
        return json.dumps(({'success': False, 'message': 'submission unsuccessful'}, response.status_code, {'Content-Type': 'application/text'}))
    
# @app.route('/contribs/<int:year>', methods=['GET'])
# @app.route('/contribs', methods=['GET'])
# def get_contribs(year=None):
#     """
#     instead of client-side making the request to fetch the raw html data
#     leading as we know a CORS error this route function will instead make
#     such a request for us in order to bypass this CORS error

#     by default user will request for route /contribs thereby not specifying 
#     the year which allows our route function to return to the user the maximum
#     date and minimum year to which he can choose from
#     """
#     print(year)
    

#     url = 'https://github.com/users/08Aristodemus24/contributions' if year == None \
#     else f'https://github.com/users/08Aristodemus24/contributions?from={year}-01-01&to={year}-12-31'

#     try:
#         response = requests.get(url)
#         dom = BeautifulSoup(response.text)

#         # determine also min year and max year
#         min_year = dt.now().year
#         max_year = 0
#         contribs = []
        
#         # select all table rows and in every row select
#         # only the days and not the label of the day
#         rows = dom.find('tbody').find_all('tr')
#         print(len(rows))
#         for row in rows:
#             curr_row = []
#             days = row.find_all('td', attrs={'class': 'ContributionCalendar-day'})
#             for day in days:
#                 content = day.text.split(' ')
#                 print(content)

#                 # for edge cases if there is no content or content has no elements 
#                 # whatsoever just append null to contribs
#                 if len(content) > 1:
#                     # print(content)

#                     # some important attributes of the td element are also data-date
#                     # and data-level which both contain the date of push and the 
#                     # strength level of number of pushes the user has done in that day
#                     date = day['data-date'].split('-')
#                     level = day['data-level']

#                     curr_row.append({
#                         'pushes': 0 if content[0] == 'No' else int(content[0]),
#                         'month-name': content[3],
#                         'month-num': date[1],
#                         # 'day-name': content[3].replace(',', ''),
#                         'day-num': date[2],
#                         'year': date[0],
#                         'level': level
#                     })

#                     # determine the minimum and maximum years in whole span
#                     # of github contributions timeline
#                     max_year = max_year if max_year > int(date[0]) else int(date[0])
#                     min_year = min_year if min_year < int(date[0]) else int(date[0])
#                 else:
#                     curr_row.append(None)

#             # once done appending one of the 7 rows representing each 
#             # day in a week append it to contribs
#             contribs.append(curr_row)
        
#         # if year is None meaning get all contributions 
#         # all the way from first push to recent push
#         data = [{'contribs': contribs}]
#         if year == None:
#             data[0]['min_year'] = min_year
#             data[0]['max_year'] = max_year

#         if response.status_code == 200:
#             print('retrieval successful')
#             return jsonify(data)
        
#         return json.dumps(({'success': False}, response.status_code, {'Content-Type': 'application/json'}))

#     except NameResolutionError as e:
#         return json.dumps(({'success': False, 'message': f'{e} has occured'}, response.status_code, {'Content-Type': 'application/json'}))

#     except ConnectionError as e:
#         return json.dumps(({'success': False, 'message': f'{e} has occured'}, response.status_code, {'Content-Type': 'application/json'}))

#     except MaxRetryError as e:
#         return json.dumps(({'success': False, 'message': f'{e} has occured'}, response.status_code, {'Content-Type': 'application/json'}))

@app.route('/contribs/<int:year>', methods=['GET'])
@app.route('/contribs', methods=['GET'])
def get_contribs(year=None):
    """
    instead of client-side making the request to fetch the raw html data
    leading as we know a CORS error this route function will instead make
    such a request for us in order to bypass this CORS error

    by default user will request for route /contribs thereby not specifying 
    the year which allows our route function to return to the user the maximum
    date and minimum year to which he can choose from
    """
    print(year)
    

    url = 'https://github-contributions-api.deno.dev/08Aristodemus24.json' if year == None \
    else f'https://github-contributions-api.deno.dev/08Aristodemus24.json?from={year}-01-01&to={year}-12-31'

    try:
        response = requests.get(url)
        data = json.loads(response.text)
        
        # initialized to determine also min year and max year
        min_year = dt.now().year
        max_year = 0

        # get contributions for parsing from response
        contribs = data['contributions']

        contribs_ref = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: []}
        contrib_levels = {'NONE': 0, 'FIRST_QUARTILE': 1, 'SECOND_QUARTILE': 2, 'THIRD_QUARTILE': 3, 'FOURTH_QUARTILE': 4}

        for week in contribs:
            for day in week:
                date = dt.strptime(day['date'], '%Y-%m-%d')
                day_of_week = date.weekday()

                # if a day of the week has not already 
                # been appended append it. Day of week range
                # from 0 to 6
                contribs_ref[day_of_week].append({
                    'pushes': day['contributionCount'],
                    'month-name': date.month,
                    'month-num': date.strftime('%B'),
                    'day-num': date.day,
                    'year': date.year,
                    'level': contrib_levels[day['contributionLevel']]
                })

                # determine the minimum and maximum years in whole span
                # of github contributions timeline
                max_year = max_year if max_year > date.year else date.year
                min_year = min_year if min_year < date.year else date.year

        # if year is None meaning get all contributions 
        # all the way from first push to recent push
        payload = [{'contribs': list(contribs_ref.values())}]
        if year == None:
            payload[0]['min_year'] = min_year
            payload[0]['max_year'] = max_year
    
        if response.status_code == 200:
            print('retrieval successful')
            return jsonify(payload)
        
        return json.dumps(({'success': False}, response.status_code, {'Content-Type': 'application/json'}))

    except NameResolutionError as e:
        return json.dumps(({'success': False, 'message': f'{e} has occured'}, response.status_code, {'Content-Type': 'application/json'}))

    except ConnectionError as e:
        return json.dumps(({'success': False, 'message': f'{e} has occured'}, response.status_code, {'Content-Type': 'application/json'}))

    except MaxRetryError as e:
        return json.dumps(({'success': False, 'message': f'{e} has occured'}, response.status_code, {'Content-Type': 'application/json'}))
