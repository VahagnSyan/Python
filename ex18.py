'''
ex 18
simple git implementation
add, commit, checkout, status, pull, push
ga, gc, gch, gss, gl, gp
ամեն մեկը տառբեռ ձևով պետք է աշխատի՝ կախված մուտքային տվյալնեռից
ու բնականաբար տարբեռ նախադասությամբ պետք ա պատասխանի օգտագործողին
'''

import sys

staging_area = []
current_branch = "main"
remote_repository = []

def ga(*files):
    staging_area.extend(files)
    return f"Added {', '.join(files)} to staging area."

def gc(message):
    global staging_area, current_branch, remote_repository
    if not staging_area:
        return "No changes to commit."

    commit_message = f"Commit '{message}' on branch '{current_branch}'"
    remote_repository.append({"branch": current_branch, "message": commit_message})
    staging_area = []
    return f"Committed changes: {commit_message}"

def gch(branch_name):
    global current_branch
    current_branch = branch_name
    return f"Switched to branch '{branch_name}'."

def gss():
    return f"Current branch: {current_branch}\nStaging area: {', '.join(staging_area)}"

def gl():
    return "Everythig olready uptodateing"

def gp():
    return "Pushed changes to remote repository."
def gs():
    return f"Staging_area is empty"
def process_git_command(command, *args, **kwargs):
    if command == "ga":
        return ga(*args)
    elif command == "gc":
        return gc(*args)
    elif command == "gch":
        return gch(*args)
    elif command == "gss":
        return gss()
    elif command == "gl":
        return gl()
    elif command == "gp":
        return gp()
    elif command == "gs":
        return gs()
    else:
        return "Command is not valid."

# Example usage with sys.argv:
if len(sys.argv) > 1:
    git_command = sys.argv[1]
    if git_command == "git":
        if sys.argv[2] == "commit":
            git_command = "gc"
        elif sys.argv[2] == "push":
            git_command = "gp"
        elif sys.argv[2] == "pull":
            git_command = "gl"
        elif sys.argv[2] == "add":
            git_command = "ga"
        elif sys.argv[2] == "checkout":
            git_command = "gck"
        elif sys.argv[2] == "status":
            git_command = "gs"
        elif sys.argv[2] == "status" and len(sys.argv) > 3 and sys.argv[3] == "-s":
            git_command = "gss"
        elif sys.argv[2] == "status":
            git_command = "gs"
    result = process_git_command(git_command, *sys.argv[2:])
    print(result)
else:
    print("Usage: python script.py <git_command> [arguments]")
