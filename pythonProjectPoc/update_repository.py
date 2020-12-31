# updating the repository

import requests
from pprint import pprint
from scret import TOKEN_VALUE

API_URL = "https://api.github.com"
GITHUB_TOKEN = TOKEN_VALUE
HEADERS = {
    "Authorization": "token " + GITHUB_TOKEN,
    "Accept": "application/vnd.github.inertia-preview+json"
}


def update_repos():
    update = requests.patch(API_URL + "/repos/sudarshanusnale98/Testing",
                            data='{"name":"Testing_updated"}', headers=HEADERS)
    pprint(update.json())
