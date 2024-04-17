#!/usr/bin/python3
"""
This script fetches and displays information about completed tasks
"""
import json
import requests


def _id():
    """
    Fetches and displays information about completed tasks for a given user ID.
    """
    todo_url = requests.get(
        f"https://jsonplaceholder.typicode.com/todos/"
    )
    user_name_url = requests.get(
        f"https://jsonplaceholder.typicode.com/users/"
    )
    """Convert response to JSON format"""
    todo_dic = todo_url.json()
    user_name_dic = user_name_url.json()
    """" Extract completed tasks from todo list"""
    data = {

        user["id"]: [
            {
                "task": task["title"],
                "completed": task["completed"],
                "username": user["username"],
            }
            for task in todo_dic
            if task["userId"] == user["id"]
        ]
        for user in user_name_dic
    }
    with open(f"todo_all_employees.json", "w") as json_file:
        json.dump(data, json_file)


if __name__ == "__main__":
    """ Retrieve the user ID from the command-line arguments"""
    _id()
