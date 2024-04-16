#!/usr/bin/python3
"""
This script fetches and displays information about completed tasks
"""
import requests
import sys
import csv


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

    """Write task information to a CSV file"""
    csv_filename = f"{user_id}.csv"
    with open(csv_filename, mode="w") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todo_dic:
            writer.writerow(
                [(user_id), user_name_dic["username"],
                 task["completed"], task["title"]]
            )


if __name__ == "__main__":
    """Retrieve the user ID from the command-line arguments"""
    user_id = sys.argv[1]
    _id(user_id)
