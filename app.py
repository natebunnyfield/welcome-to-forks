from dotenv import load_dotenv
from flask import Flask, redirect, render_template, request
from github import Github
import os
import requests

load_dotenv()
GITHUB_CLIENT_ID = os.environ.get('GITHUB_CLIENT_ID')
GITHUB_CLIENT_SECRET = os.environ.get('GITHUB_CLIENT_SECRET')
GITHUB_ACCESS_TOKEN_URL = os.environ.get('GITHUB_ACCESS_TOKEN_URL')
GITHUB_REPO_FORK_URL = os.environ.get('GITHUB_REPO_FORK_URL')
GITHUB_OAUTH_URL = os.environ.get('GITHUB_OAUTH_URL')
GITHUB_REPO_PATH = os.environ.get('GITHUB_REPO_PATH')

app = Flask(__name__)

@app.route('/')
def github():
    """"""
    page_data = {
        'github_fork_url': GITHUB_REPO_FORK_URL,
        'github_oauth_url': GITHUB_OAUTH_URL,
        'github_client_id': GITHUB_CLIENT_ID,
        'github_scope': 'user:email public_repo',
    }
    return render_template('app.html', **page_data)

@app.route('/oauth/callback')
def oauth_callback():
    """"""
    request_token = request.args.get('code')

    post_data = {
        'client_id': GITHUB_CLIENT_ID,
        'client_secret': GITHUB_CLIENT_SECRET,
        'code': request_token,
    }
    res = requests.post(GITHUB_ACCESS_TOKEN_URL, json=post_data, headers={'Accept': 'application/json'})
    res_data = res.json()
    access_token = res_data.get('access_token')

    gh = Github(access_token)
    user = gh.get_user()
    repo = gh.get_repo(GITHUB_REPO_PATH)
    forked_repo = user.create_fork(repo)

    return redirect(forked_repo.html_url)