# Intro
Simple script to clone all Gitlab repos (including private ones) that you have access to. 

# Requirements
Uses os, subprocess, python-gitlab, sys, shutil on python 3.
```
pip3 install python-gitlab
```

* Other packages should be installed/available by default.

# Setup
It uses gitlab API, so you need to get access tokens by going to Settings > Access tokens. Select api, read_user, read_repository checkboxes under scopes. Click on Create personal access token. 

* Replace **YOUR_PRIVATE_TOKEN** in the code with your access token.
* Replace **gitlab_url** variable's value with your gitlab server URL.
* By default, this script only gets **PRIVATE repos**. To get all repos, remove *visibility='private'* from line 38. For more information and available options, see [python-gitlab docs](https://python-gitlab.readthedocs.io/en/stable/gl_objects/projects.html).  

# Use
```
python3 getlab.py [username] [password] [optional path]
```
* *username and password* are the login combination that you use to login to the gitlab server. 

* *optional_path* is the absolute path of the destination directory to clone the repositories to. If not provided, it will use the current path.


