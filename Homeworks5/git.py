"""
    Simple git implementation.
"""


from sys import argv, exit


def convert_args_to_string(args):
    # function converts args which is array to string
    # that consist from args elements
    string_args = ""
    for arg in args:
        string_args += arg + " "
    return string_args


def add(files):
    if files:
        string_files = convert_args_to_string(files)
        print(f"Added {string_files}to stage.")


def commit(message):
    if message:
        string_message = convert_args_to_string(message)
        print(f"Commit with message ' {string_message}' created successfully!")


def checkout(branch):
    if branch:
        print(f"Successfully switched to branch - {branch}")


def status():
    print(f"Changes not staged for commit.")


def pull(branch):
    if branch:
        print(f"Workspace {branch} updated successfully.")


def push():
    print("Pushed current branch to github.")


if len(argv) <= 1:
    print("Please provide action name.")
    exit()

if argv[1] == "add" or argv[1] == "ga":
    if argv[2:]:
        add(argv[2:])
    else:
        print("Please provide arguments.")

if argv[1] == "commit" or argv[1] == "gc":
    if argv[2:]:
        commit(argv[2:])
    else:
        print("Please provide arguments.")

if argv[1] == "checkout" or argv[1] == "gch":
    if argv[2:]:
        checkout(argv[2])
    else:
        print("Please provide arguments.")


if argv[1] == "status" or argv[1] == "gss":
    status()

if argv[1] == "pull" or argv[1] == "gl":
    if argv[2:]:
        pull(argv[2])
    else:
        print("Please provide arguments.")

if argv[1] == "push" or argv[1] == "gp":
    push()
