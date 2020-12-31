# Creating new projct in repository.

import requests
from pprint import pprint
from scret import TOKEN_VALUE

API_URL = "https://api.github.com"
GITHUB_TOKEN = TOKEN_VALUE
HEADERS = {
    "Authorization": "token " + GITHUB_TOKEN,
    "Accept": "application/vnd.github.inertia-preview+json"
}

data = requests.post(API_URL + "/repos/sudarshanusnale98/poc/projects",
                     data='{"name":"Testing_Again"}', headers=HEADERS)
pprint(data.json())
