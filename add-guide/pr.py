from github import Github 
from github import Auth 
from dotenv import load_dotenv
import os 
import random 
import ocr
import datetime

load_dotenv() 

auth = Auth.Token(os.getenv('access'))
g = Github(auth=auth) 
username = g.get_user().login

garden = g.get_repo(f"{username}/garden")
print(garden)

# create branch and commit 
main = garden.get_branch("main") 
text = ocr.get_text('md.png')
guide_name = text[0:text.index("\n")].strip("# ")
filename = guide_name.replace(' ', '-')
branch = garden.create_git_ref(f"refs/heads/add-{filename}", main.commit.sha)
frontmatter = f"""+++
title = {guide_name}
date = {datetime.datetime.now()}
draft = false
+++

"""
content = frontmatter + text
path = f"content/guides/{filename}.md"
message = f"Add {filename}.txt"
garden.create_file(path, message, content, branch.ref)

# create PR 
title = "auto: Add guide" 
body = """
Add new plant-name guide 
""" 
pr = garden.create_pull(title=title, body=body, head=branch.ref, base=main.name)

