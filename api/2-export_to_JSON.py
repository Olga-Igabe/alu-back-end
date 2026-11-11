#!/usr/bin/python3
"""Export an employee's TODO list to a JSON file using a REST API."""
import json
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = int(sys.argv[1])
    user = requests.get(url + "users/{}".format(user_id)).json()
    todos = requests.get(url + "todos", params={"userId": user_id}).json()
    username = user.get("username")

    data = {str(user_id): [{"task": task.get("title"),
                            "completed": task.get("completed"),
                            "username": username} for task in todos]}

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump(data, jsonfile)
