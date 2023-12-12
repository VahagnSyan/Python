"""
Git simple implementation
"""


import sys


def add(files):
    if not files:
        print("No files provided for 'add' operation.")
        return
    print("Added:", ", ".join(files))


def commit(message):
    if not message:
        print("No commit message provided.")
        return
    print("Committed with message:", " ".join(message))


def pull():
    print("Already up to date.")


def push():
    print("Pushed:")


def checkout(arguments):
    if arguments[0] != "-b":
        print("Invalid arguments:")
        sys.exit(1)
    branch = arguments[1]
    print(f"Branch switched to {branch}")


def status():
    print("You are on branch main:")


def main():
    args = sys.argv

    if len(args) == 1:
        print("Not enough arguments provided")
        sys.exit(1)

    commands = [
        "add",
        "ga",
        "commit",
        "gc",
        "gp",
        "push",
        "status",
        "gss",
        "gl",
        "pull",
        "checkout",
        "gch",
    ]
    command = sys.argv[1]
    if not command in commands:
        print("Invalid command:")
        sys.exit(1)

    if len(args) < 3 and (
        args[1] != "pull"
        and args[1] != "gl"
        and args[1] != "push"
        and args[1] != "gp"
        and args[1] != "status"
        and args[1] != "gss"
    ):

        print("Not enough arguments provided.")
        sys.exit(1)

    command = sys.argv[1]
    arguments = sys.argv[2:]

    if command == "add" or command == "ga":
        add(arguments)
    elif command == "commit" or command == "gc":
        commit(arguments)
    elif command == "pull" or command == "gl":
        pull()
    elif command == "checkout" or command == "gch":
        checkout(arguments)
    elif command == "status" or command == "gss":
        status()


if __name__ == "__main__":
    main()

