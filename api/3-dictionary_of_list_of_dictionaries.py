#!/usr/bin/python3
"""Export the TODO lists of all employees to a JSON file."""
import json
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()

    data = {}
    for user in users:
        user_id = user.get("id")
        todos = requests.get(url + "todos",
                             params={"userId": user_id}).json()
        data[str(user_id)] = [{"username": user.get("username"),
                               "task": task.get("title"),
                               "completed": task.get("completed")}
                              for task in todos]

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(data, jsonfile)
