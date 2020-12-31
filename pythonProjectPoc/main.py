from github import Github

class Git_hub():
    global g,username,password
    # username=input("Enter username:")
    # password=input("Enter password:")

    g=Github("20b4170bd537ad180c1d95e7c0d6bdf8d5e547c8")

    def get_repos(self):
        repos=g.get_user().get_repos()
        for repo in repos:
            print(repo.name)

    def get_user(self):
     user = g.get_user()
     print(user.login)

    def get_user_byname(self):
     user = g.get_user("preranaagale")
     print(user.name)

    def get_repo_byname(self):
     repo=g.get_repo("preranaagale/LP3")
     print(repo.name)
     print(repo.get_views_traffic())

    def get_content(self):
     repo = g.get_repo("preranaagale/LP3")
     contents=repo.get_contents("rsa")  #specific file
     for content in contents:
       print(content)

    def create_new_repo(self):
     try:
       user=g.get_user()
       repo = user.create_repo("Test")
     except:
      print("Repository already exists")
     else:
      print("Repository created successfully")

    def add_file_torepo(self):
     try:
      repo = g.get_repo("preranaagale/Test")
      repo.create_file("test.txt", "test", "test", branch="test")
     except:
      print("Cannot add file")
     else:
      print("File added!!")


    def update_file(self):
     try:
      repo = g.get_repo("preranaagale/Test")
      contents = repo.get_contents("test.txt", ref="test")
      repo.update_file(contents.path, "this is text", "this is text", contents.sha, branch="test")
     except:
      print("cannot update")
     else:
      print("Updated")


    def delete_file(self):
     try:
      repo = g.get_repo("preranaagale/Test")
      contents = repo.get_contents("test.txt", ref="test")
      repo.delete_file(contents.path, "remove test", contents.sha, branch="test")
     except:
      print("cannot delete")
     else:
      print("Deleted")




p=Git_hub()

p.get_user()
p.get_user_byname()
p.get_repos()
p.get_repo_byname()
p.get_content()
p.create_new_repo()
p.add_file_torepo()
p.update_file()
p.delete_file()
