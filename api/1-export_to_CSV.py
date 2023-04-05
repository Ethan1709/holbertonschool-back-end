#!/usr/bin/python3
"""
Writes a Python script that, using this REST API, for
a given employee ID, returns information about his/her TODO list progress.
"""

import csv
import json
import requests
import sys


if __name__ == "__main__":

    response_user = requests.get('https://jsonplaceholder.typicode.com/users')
    response_todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    user = response_user.json()
    todos = response_todos.json()

    for item in user:
        if 'id' in item and str(item.get('id')) == str(sys.argv[1]):
            n = item.get('id')
            u_n = item.get('username')

    with open(str(sys.argv[1]) + ".csv", 'w') as f:
        csv_file = csv.writer(f)
        for item in todos:
            if 'userId' in item\
                  and str(item.get('userId')) == str(sys.argv[1]):
                li = []
                li.append(n)
                li.append(u_n)
                li.append(item.get('completed'))
                li.append(item.get('title'))
                csv_file.writerow(li)
