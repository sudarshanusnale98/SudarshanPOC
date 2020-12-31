# GitHub API Research In Python

In Github API research you can execute creating new project - repository,
read the existing project - repositories also can update the same. For this
have used the token authentication. Where you have to create your key from the
Github account and save that into the variable in secret.py file. It implements 
the Github API research in python.

## Install

    python
    pycharm (editor)

## Run & Test

    For running the file index.py to execute github api research.

# REST API

The REST API to the example is described below.

## Create a new Thing

### Request

`POST /thing/`

    https://api.github.com/user/repos

### Response

    Creates the new github repository.

## Get a specific Thing

### Request

`GET /thing/id`

    https://api.github.com/users/sudarshanusnale

### Response

    Response will give the details of specific user here ex. sudarshanusnale

## Delete a Thing

### Request

`DELETE /thing/id`

    https://api.github.com/repos/sudarshanusnale98/poc

### Response

  Delete the specific repository.



