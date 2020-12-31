# Updating the repository.

import requests
from pprint import pprint
from scret import TOKEN_VALUE

API_URL = "https://api.github.com"
GITHUB_TOKEN = TOKEN_VALUE
payload = '{"name" = "TestName"}'
headers = {
    "Authorization": "token " + GITHUB_TOKEN,
    "Accept": "application/vnd.github.inertia-preview+json"
}


def updateRepos():
    update = requests.patch(API_URL + "/repos/sudarshanusnale98/poc",
                            data='{"name":"Testing_1"}', headers=headers)
    pprint(update.json())
