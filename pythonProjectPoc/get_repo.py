# Fetching the repositories

import requests
from pprint import pprint
from scret import TOKEN_VALUE

API_URL = "https://api.github.com"
GITHUB_TOKEN = TOKEN_VALUE
HEADERS = {
    "Authorization": "token " + GITHUB_TOKEN,
    "Accept": "application/vnd.github.inertia-preview+json"
}


def get_repos():
    data = requests.get(API_URL + "/users/sudarshanusnale98/repos",
                        headers=HEADERS)
    pprint(data.json())
