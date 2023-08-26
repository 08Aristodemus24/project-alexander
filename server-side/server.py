from flask import Flask
from pathlib import Path

# ff. imports are for getting secret values from .env file
import os
from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
env_dir = Path('./').resolve()
load_dotenv(os.path.join(env_dir, '.env'))


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    """
    flask app will run at http://127.0.0.1:5000 if /
    in url succeeds another string <some string> then
    app will run at http://127.0.0.1:5000/<some string>

    returns .json file of the github access token upon
    request to the route
    """

    return {
        'gat': os.environ['GITHUB_ACCESS_TOKEN']
    }
