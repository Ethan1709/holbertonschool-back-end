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
        n = str(item.get('id'))
        u_n = item.get('username')
        li = []
        for i in todos:
            if i.get('userId') == item.get('id'):
                new_d = {}
                new_d['username'] = u_n
                new_d['task'] = i.get('title')
                new_d['completed'] = i.get('completed')
                li.append(new_d)
        d[n] = li

    with open("todo_all_employees.json", 'w') as f:
        json.dump(d, f)
