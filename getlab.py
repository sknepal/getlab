##Subigya Nepal
##Mon Apr 8, 2019, 2.37 AM
import os, subprocess, gitlab, sys, shutil
  
def main():
    gitlab_url = 'https://gitlab.cs.dartmouth.edu' #enter your custom gitlab url
    private_token = 'YOUR_PRIVATE_TOKEN' #settings > access tokens > api, read_user, read_repo > create
    
    if len(sys.argv) == 4:
        username = sys.argv[1]
        password = sys.argv[2]
        visibility = sys.argv[3] ##absolute path
        path = '.'
    elif len(sys.argv) == 5:
        username = sys.argv[1]
        password = sys.argv[2]
        visibility = sys.argv[3]
        path = sys.argv[4]
    else:
        print("Please pass arguments in this format: username password visibility optional_absolute_path.\nAt least two arguments required.")
        sys.exit(0)

    try:
        auth_obj = git_auth(gitlab_url, private_token)
        give_me_repos(auth_obj, username, password, path, visibility)
    except Exception as e:
        print(e)
        print("\nAre you sure you provided correct username/password/token combination?\n")
        

def git_auth(gitlab_url, private_token):
    gl = gitlab.Gitlab(gitlab_url, private_token=private_token, api_version=4)
    gl.auth()
    print("Authenticated via Token")
    print("=============\n")
    return gl

def give_me_repos(gl, username, password, path, visibility='all'):
    progress = 0
    if (visibility=='all'):
        projects = gl.projects.list(all=True)
    else:  
        projects = gl.projects.list(visibility=visibility, all=True)
    for project in projects:
        dir_name = project.path
        if os.path.exists(os.path.join(path, dir_name)):
            shutil.rmtree(os.path.join(path, dir_name))
        git_url = 'https://' + username + ':' + password + '@' + project.http_url_to_repo.split("https://")[1]
        do_your_thing = subprocess.call(['git', 'clone', git_url], cwd=path, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        progress+= 1
        print('Progress: {}/{} repos processed'.format(progress, len(projects)))
        
if __name__ == "__main__":
    main()