# Deleting the project.

import requests
from pprint import pprint
from scret import TOKEN_VALUE

API_URL = "https://api.github.com"
GITHUB_TOKEN = TOKEN_VALUE
HEADERS = {
    "Authorization": "token " + GITHUB_TOKEN,
    "Accept": "application/vnd.github.inertia-preview+json"
}


def delete_project():
    delete_project_value = requests.delete(API_URL + "/projects/5875141",
                                           headers=HEADERS)
    pprint(delete_project_value.text)


