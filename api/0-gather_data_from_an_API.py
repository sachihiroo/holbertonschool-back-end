#!/usr/bin/python3
"""
This script fetches and displays information about completed tasks
"""
import requests
import sys


def _id(user_id):
    """
    Fetches and displays information about completed tasks for a given user ID.
    """
    todo_url = requests.get(
        f"https://jsonplaceholder.typicode.com/todos/?userId={user_id}"
    )
    user_name_url = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{user_id}"
    )
    """Convert response to JSON format"""
    todo_dic = todo_url.json()
    user_name_dic = user_name_url.json()
    """" Extract completed tasks from todo list"""
    _comp = []
    for i in todo_dic:
        if i["completed"]:
            _comp.append(i["title"])
    """ Display the user's name and completed tasks"""
    print(f"Employee {user_name_dic['name']} is done with tasks \
({len(_comp)}/{len(todo_dic)}):")
    for task in _comp:
        print(f"\t {task}")


if __name__ == "__main__":
    """ Retrieve the user ID from the command-line arguments"""
    user_id = sys.argv[1]
    _id(user_id)
