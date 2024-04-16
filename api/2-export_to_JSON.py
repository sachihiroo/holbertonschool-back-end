#!/usr/bin/python3
"""
This script fetches and displays information about completed tasks
"""
import json
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
    data = {

        user_id: [
            {
                "username": user_name_dic["username"],
                "task": task["title"],
                "completed": task["completed"],
            }
            for task in todo_dic
        ]
    }
    with open(f"{user_id}.json", "w") as jsonfile:
        json.dump(data, jsonfile)


if __name__ == "__main__":
    """ Retrieve the user ID from the command-line arguments"""
    user_id = sys.argv[1]
    _id(user_id)
