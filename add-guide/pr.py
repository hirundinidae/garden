from github import Github 
from github import Auth 
from dotenv import load_dotenv
import os 
import random 

load_dotenv() 

auth = Auth.Token(os.getenv('access'))
g = Github(auth=auth) 
username = g.get_user().login

garden = g.get_repo(f"{username}/garden")
print(garden)

# create branch and commit 
main = garden.get_branch("main") 
branch = garden.create_git_ref(f"refs/heads/test-branch-{random.random()}", main.commit.sha)
path = "test.txt" 
message = "test commit with test.txt" 
content = """
#title 
## description 
"""
garden.create_file(path, message, content, branch.ref)

# create PR 
title = "auto: Add guide" 
body = """
Add new plant-name guide 
""" 
pr = garden.create_pull(title=title, body=body, head=branch.ref, base=main.name)

