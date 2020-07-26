#!/usr/bin/env python
import os
import urllib
from uuid import uuid4

import requests
import requests.auth
from flask import Flask, abort, request, render_template, redirect

CLIENT_ID = os.environ['CLIENT_ID']
CLIENT_SECRET = os.environ['CLIENT_SECRET']  # Fill this in with your client secret
REDIRECT_URI = os.environ['REDIRECT_URI']

global bucket_id
global slack_webhook
global team_id


def user_agent():
    return "Get notifs to your slack space (advait.live)"


def base_headers():
    return {"User-Agent": user_agent()}


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def homepage():
    global bucket_id
    global slack_webhook
    global team_id
    if request.method == 'POST':
        bucket_id = request.form['bucketId']
        slack_webhook = request.form['webhook']
        team_id = request.form['teamId']
        return redirect(make_authorization_url())
    return render_template('index.html')


def make_authorization_url():
    # Generate a random string for the state parameter
    # Save it for use later to prevent xsrf attacks
    state = str(uuid4())
    save_created_state(state)
    params = {"client_id": CLIENT_ID,
              "redirect_uri": REDIRECT_URI,
              "type": "web_server"
              }
    url = "https://launchpad.37signals.com/authorization/new?" + urllib.parse.urlencode(params)
    return url


# Left as an exercise to the reader.
# You may want to store valid states in a database or memcache.
def save_created_state(state):
    pass


def is_valid_state(state):
    return True


@app.route('/test')
def basecamp_callback():
    error = request.args.get('error', '')
    if error:
        return "Error: " + error
    state = request.args.get('state', '')
    if not is_valid_state(state):
        # Uh-oh, this request wasn't started by us!
        abort(403)
    code = request.args.get('code')
    access_token = get_token(code)
    # Note: In most cases, you'll want to store the access token, in, say,
    # a session for use in other parts of your web app.
    status = register_webhook(access_token)
    if status == 201:
        return "Success"
    else:
        return "Internal Error"


@app.route('/webhook')
def notif_webhook():
    print(request)


def get_token(code):
    client_auth = requests.auth.HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)
    post_data = {"grant_type": "authorization_code",
                 "code": code,
                 "redirect_uri": REDIRECT_URI,
                 "client_id": CLIENT_ID,
                 "redirect_uri": REDIRECT_URI,
                 "client_secret": CLIENT_SECRET,
                 "type": "web_server"
                 }
    headers = base_headers()
    response = requests.post("https://launchpad.37signals.com/authorization/token",
                             auth=client_auth,
                             headers=headers,
                             data=post_data)
    token_json = response.json()
    return token_json["access_token"]


def register_webhook(access_token):
    headers = base_headers()
    headers.update({"Authorization": "bearer " + access_token})
    post_data = {
        "payload_url": slack_webhook}
    response = requests.post("https://3.basecampapi.com/" + team_id + "/buckets/" + bucket_id + "/webhooks.json",
                             headers=headers,
                             json=post_data)
    return response.status_code


if __name__ == '__main__':
    app.run(debug=True, port=65010, ssl_context='adhoc')
