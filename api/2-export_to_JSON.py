#!/usr/bin/python3
"""
Writes a Python script that, using this REST API, for
a given employee ID, returns information about his/her TODO list progress.
"""

import json
import requests
import sys


if __name__ == "__main__":

    response_user = requests.get('https://jsonplaceholder.typicode.com/users')
    response_todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    user = response_user.json()
    todos = response_todos.json()

    d = {}
    for item in user:
        if 'id' in item and str(item.get('id')) == str(sys.argv[1]):
            n = item.get('id')
            u_n = item.get('username')

    li = []
    for item in todos:
        if 'userId' in item and str(item.get('userId')) == str(sys.argv[1]):
            new_d = {}
            t = item.get('title')
            c = str(item.get('completed'))
            new_d.update({"task": t})
            new_d.update({"completed": c})
            new_d.update({"username": u_n})
            li.append(new_d)

    d[n] = li
    print(d)
