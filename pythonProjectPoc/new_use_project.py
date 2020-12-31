# Creating new user projects.

import requests
from pprint import pprint
from scret import TOKEN_VALUE

API_URL = "https://api.github.com"
GITHUB_TOKEN = TOKEN_VALUE
HEADERS = {
    "Authorization": "token " + GITHUB_TOKEN,
    "Accept": "application/vnd.github.inertia-preview+json"
}


def user_project():
    data = requests.post(API_URL + "/user/projects",
                         data='{"name":"New_user_Proj111"}', headers=HEADERS)
    pprint(data.json())
