#!/usr/bin/python3
"""Exports all employees' TODO list data to a JSON file."""
import collections
import json
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    users = requests.get(url + "users").json()
    todos = requests.get(url + "todos").json()

    data = collections.OrderedDict()
    for user in users:
        user_id = user.get("id")
        username = user.get("username")
        tasks = []
        for task in todos:
            if task.get("userId") == user_id:
                item = collections.OrderedDict()
                item["username"] = username
                item["task"] = task.get("title")
                item["completed"] = task.get("completed")
                tasks.append(item)
        data[str(user_id)] = tasks

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(data, jsonfile)
