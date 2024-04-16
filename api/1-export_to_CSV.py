#!/usr/bin/python3
"""
This script will use the REST API to return information
about a given employee's TODO list progress.
"""
import pandas as pd
import requests
import sys


def TODO_REQUESTS(ID):
    """
    extend your Python script to export data in the CSV format
    """
    todos = requests.get(
        f"https://jsonplaceholder.typicode.com/todos?userId={ID}"
    ).json()
    user_info = requests.get(
        f"https://jsonplaceholder.\
typicode.com/users/{ID}"
    ).json()
    df = pd.DataFrame(todos)
    df["username"] = user_info["username"]
    df = df[["userId", "username", "completed", "title"]]
    df.to_csv(f"{ID}.csv", index=False, quoting=1)


if __name__ == "__main__":
    ID = sys.argv[1]
    TODO_REQUESTS(ID)
