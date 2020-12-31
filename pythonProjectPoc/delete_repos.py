# Deleting the repository.

import requests
from pprint import pprint
from scret import TOKEN_VALUE

API_URL = "https://api.github.com"
GITHUB_TOKEN = TOKEN_VALUE
HEADERS = {
    "Authorization": "token " + GITHUB_TOKEN,
    "Accept": "application/vnd.github.inertia-preview+json"
}


def delete_repos():
    data = requests.delete(API_URL + "/repos/sudarshanusnale98/Testing11",
                           data='{"name":"New_repos1"}',
                           headers=HEADERS)
    pprint(data)
