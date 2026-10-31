#!/usr/bin/python3
"""Exports an employee's TODO list data to a JSON file."""
import collections
import json
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]

    user = requests.get(url + "users/{}".format(user_id)).json()
    todos = requests.get(url + "todos", params={"userId": user_id}).json()
    username = user.get("username")

    tasks = []
    for task in todos:
        item = collections.OrderedDict()
        item["task"] = task.get("title")
        item["completed"] = task.get("completed")
        item["username"] = username
        tasks.append(item)

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump({user_id: tasks}, jsonfile)
