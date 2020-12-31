# GitHub API implementation

from user_detail import user_details
from get_repo import get_repos
from new_repository import new_repos
from update_repository import update_repos
from delete_repos import delete_repos
from get_projects import get_project
from new_use_project import user_project
from update_project import update_project
from delete_project import delete_project

print(
    "\n1.Get user details\n2.Get repos\n3.create Repo\n4.Update Rpo\n"
    "5.Delete Repo\n6.Get projects\n7.Create "
    "project\n8.Update project\n8.Delete project\n")

while True:

    num = int(input("\n\nEnter your choice (or 0 to quit):"))

    if num == 0:
        break
    elif num == 1:
        user_details()
        break
    elif num == 2:
        get_repos()
        break
    elif num == 3:
        new_repos()
        break
    elif num == 4:
        update_repos()
        break
    elif num == 5:
        try:
            response = delete_repos()
        except:
            print("Cannot delete repo!!")
        else:
            print(response.text)
    elif num == 6:
        get_project()
        break
    elif num == 7:
        user_project()
        break
    elif num == 8:
        update_project()
        break
    elif num == 9:
        delete_project()
        break
    else:
        print("enter correct option: ")
        print("\n")