# Creating new repository.

import requests
from pprint import pprint
from scret import TOKEN_VALUE

API_URL = "https://api.github.com"
GITHUB_TOKEN = TOKEN_VALUE
HEADERS = {
    "Authorization": "token " + GITHUB_TOKEN,
    "Accept": "application/vnd.github.inertia-preview+json"
}


def new_repos():
    data = requests.post(API_URL + "/user/repos",
                         data='{"name":"Testing}', headers=HEADERS)
    pprint(data.json())
