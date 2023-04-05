#!/usr/bin/python3
"""
Writes a Python script that, using this REST API, for
a given employee ID, returns information about his/her TODO list progress.
"""

from requests import get
import sys


if __name__ == "__main__":

    response_user = get('https://jsonplaceholder.typicode.com/users')
    response_todos = get('https://jsonplaceholder.typicode.com/todos')
    user = response_user.json()
    todos = response_todos.json()

    for item in user:
        if 'id' in item and str(item.get('id')) == str(sys.argv[1]):
            n = item.get('id')
    n -= 1

    i = 0
    j = 0
    li = []
    for item in todos:
        if 'userId' in item and str(item.get('userId')) == str(sys.argv[1]):
            if item.get('completed') is True:
                i += 1
                li.append(item.get('title'))
            else:
                j += 1

    EMPLOYEE_NAME = user[n]['name']
    NUMBER_OF_DONE_TASKS = i
    TOTAL_NUMBER_OF_TASKS = i + j
    TASK_TITLE = ""
    print('Employee {} is done with tasks({}/{}):'.format
          (EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
    for i in li:
        TASK_TITLE = i
        print('\t ' + TASK_TITLE)
