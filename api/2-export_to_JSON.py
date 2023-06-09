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
            n = str(item.get('id'))
            u_n = item.get('username')

    li = []
    for item in todos:
        if 'userId' in item and str(item.get('userId')) == str(sys.argv[1]):
            new_d = {}
            new_d['task'] = item.get('title')
            new_d['completed'] = item.get('completed')
            new_d['username'] = u_n
            li.append(new_d)

    d[n] = li

    with open(str(sys.argv[1]) + ".json", 'w') as f:
        json.dump(d, f)
