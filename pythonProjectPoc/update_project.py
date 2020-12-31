# Updating the projects.

import requests
from pprint import pprint
from scret import TOKEN_VALUE

API_URL = "https://api.github.com"
GITHUB_TOKEN = TOKEN_VALUE
HEADERS = {
    "Authorization": "token " + GITHUB_TOKEN,
    "Accept": "application/vnd.github.inertia-preview+json"
}


def update_project():
    update = requests.patch(API_URL + "/projects/5874854",
                            data='{"name":"Testing_up"}', headers=HEADERS)
    pprint(update.json())
