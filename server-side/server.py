import base64
import requests
import json

from email.mime.text import MIMEText
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

from requests.exceptions import ConnectionError
from urllib3.exceptions import MaxRetryError, NameResolutionError
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
CORS(app, origins=["http://127.0.0.1:5500", "http://127.0.0.1:5000", "http://localhost:5173", "http://127.0.0.1:5173", "https://project-alexander.vercel.app"])

# define variables for github data
GITHUB_USERNAME = "08Aristodemus24"
GITHUB_GRAPHQL_URL = "https://api.github.com/graphql"
CONTRIB_LEVELS = {
    'NONE': 0,
    'FIRST_QUARTILE': 1,
    'SECOND_QUARTILE': 2,
    'THIRD_QUARTILE': 3,
    'FOURTH_QUARTILE': 4
}

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

    # # if no limit is provided for number 
    # # of repos to fetch use default of 30
    # url = "https://api.github.com/users/08Aristodemus24/repos{}".format('' if repo_limit == None else f'?per_page={repo_limit}')
    # accept = 'application/vnd.github+json'
    # auth_token = f"Bearer {os.environ['GITHUB_ACCESS_TOKEN']}"
    # headers = {
    #     "Accept": accept,
    #     # "Authorization": auth_token
    # }
    # response = requests.get(url, headers=headers)
    
    url = "https://api.github.com/users/08Aristodemus24/repos{}".format('' if repo_limit == None else f'?per_page={repo_limit}')
    response = requests.get(url)
    data = response.json()

    # check if response returns an 'ok' (200) status 
    if response.status_code == 200:
        print(data)
        return data
    
    # if error occurs in request just return the key value
    # pairs of the response.json() dictionary and the status
    # code of the response object
    return json.dumps({'success': False}, response.status_code, {'Content-Type': 'application/json'})


def get_gmail_service():
    """
    Rebuilds Gmail API credentials from the long-lived refresh token
    stored in environment variables, then returns an authorized
    Gmail API client. The account these credentials belong to is
    always the one actually sending the message — Gmail does not
    let you send "as" an arbitrary address just by setting a header.
    """
    creds = Credentials(
        token=None,
        refresh_token=os.environ['GMAIL_REFRESH_TOKEN'],
        client_id=os.environ['GMAIL_CLIENT_ID'],
        client_secret=os.environ['GMAIL_CLIENT_SECRET'],
        token_uri='https://oauth2.googleapis.com/token',
        scopes=['https://www.googleapis.com/auth/gmail.send'],
    )
    return build('gmail', 'v1', credentials=creds)


def build_message(raw_data):
    """
    Formats the form submission into an email addressed to
    GMAIL_RECEIVER (your inbox). The 'from' and 'reply-to' headers
    both use the email address the visitor typed into the form
    (raw_data['email_address']) rather than a fixed env var, so you
    can reply straight to whoever submitted the form.

    Note: Gmail will still show the message as sent by your
    authenticated account (the one behind GMAIL_REFRESH_TOKEN) —
    it doesn't let a 'from' header spoof an address you don't own.
    Setting it to the visitor's email here mainly makes the
    reply-to behavior explicit and keeps the header human-readable;
    the practical "reply to the visitor" behavior comes from the
    reply-to header either way.
    """
    sender_email = raw_data.get('email_address')

    body = (
        f"First name: {raw_data.get('first_name')}\n"
        f"Last name: {raw_data.get('last_name')}\n"
        f"Email: {sender_email}\n"
        f"Phone: {raw_data.get('country_code')} {raw_data.get('mobile_num')}\n\n"
        f"Message:\n{raw_data.get('message')}"
    )

    message = MIMEText(body)
    message['to'] = os.environ['GMAIL_RECEIVER']
    message['from'] = f"Project Alexander Client <{sender_email}>"
    message['subject'] = f"{raw_data.get('first_name')} {raw_data.get('last_name')} has messaged you"
    message['reply-to'] = sender_email

    raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
    return {
        'raw': raw
    }


@app.route('/send-mail', methods=['POST'])
def send_mail():
    """
    Catches the HTTP POST request from the form in the front end
    and sends the submission as an email via the Gmail API, using
    the visitor's own submitted email as the from/reply-to address.
    """
    raw_data = request.json
    print(type(raw_data))
    print(raw_data)

    try:
        service = get_gmail_service()
        message = build_message(raw_data)
        service.users().messages().send(userId='me', body=message).execute()

        print('submission successful')
        return json.dumps(({'success': True, 'message': 'submission successful'}, 200, {'Content-Type': 'application/text'}))

    except Exception as e:
        print(f'submission unsuccessful.\nerror: {e}')
        return json.dumps(({'success': False, 'message': 'submission unsuccessful'}, 500, {'Content-Type': 'application/text'}))

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

def _graphql_request(query, variables):
    headers = {
        "Authorization": f"Bearer {os.environ['GITHUB_ACCESS_TOKEN']}",
        "Content-Type": "application/json"
    }
    resp = requests.post(GITHUB_GRAPHQL_URL, json={"query": query, "variables": variables}, headers=headers)
    resp.raise_for_status()
    payload = resp.json()
    if 'errors' in payload:
        raise ValueError(payload['errors'])
    return payload

def _get_account_created_at(username):
    resp = requests.get(f"https://api.github.com/users/{username}")
    resp.raise_for_status()
    return dt.strptime(resp.json()['created_at'], '%Y-%m-%dT%H:%M:%SZ')

def _fetch_contribution_days(username, start, end):
    query = """
        query($login: String!, $from: DateTime!, $to: DateTime!) {
            user(login: $login) {
                    contributionsCollection(from: $from, to: $to) {
                    contributionCalendar {
                        weeks {
                            contributionDays {
                                date
                                contributionCount
                                contributionLevel
                            }
                        }
                    }
                }
            }
        }
    """
    variables = {
        "login": username,
        "from": start.strftime('%Y-%m-%dT00:00:00Z'),
        "to": end.strftime('%Y-%m-%dT23:59:59Z')
    }
    result = _graphql_request(query, variables)
    weeks = result['data']['user']['contributionsCollection']['contributionCalendar']['weeks']
    days = []
    for week in weeks:
        days.extend(week['contributionDays'])
    return days


@app.route('/contribs/<int:year>', methods=['GET'])
@app.route('/contribs', methods=['GET'])
def get_contribs(year=None):
    """
    Fetches GitHub contribution data via the official GraphQL API instead
    of scraping or relying on third-party mirrors. If no year is given,
    walks year-by-year from account creation to now, since a single
    contributionsCollection query is capped at a 1-year window.
    """
    try:
        created_at = _get_account_created_at(GITHUB_USERNAME)
        min_year = created_at.year
        max_year = dt.now().year

        if year is not None:
            start = dt(year, 1, 1)
            end = dt(year, 12, 31)
            print(start)
            all_days = _fetch_contribution_days(GITHUB_USERNAME, start, end)
        else:
            all_days = []
            for y in range(min_year, max_year + 1):
                start = created_at if y == min_year else dt(y, 1, 1)
                end = dt.now() if y == max_year else dt(y, 12, 31)
                all_days.extend(_fetch_contribution_days(GITHUB_USERNAME, start, end))

        contribs_ref = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: []}
        for day in all_days:
            date = dt.strptime(day['date'], '%Y-%m-%d')
            contribs_ref[date.weekday()].append({
                'pushes': day['contributionCount'],
                'month-name': date.strftime('%B'),
                'month-num': date.month,
                'day-num': date.day,
                'year': date.year,
                'level': CONTRIB_LEVELS[day['contributionLevel']]
            })

        payload = [{'contribs': list(contribs_ref.values())}]
        if year is None:
            payload[0]['min_year'] = min_year
            payload[0]['max_year'] = max_year

        return jsonify(payload)

    except requests.exceptions.RequestException as e:
        return jsonify({'success': False, 'message': f'{e} has occured'}), 502
    except ValueError as e:
        return jsonify({'success': False, 'message': f'GraphQL error: {e}'}), 502