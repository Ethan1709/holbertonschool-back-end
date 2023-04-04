#!/usr/bin/python3
"""API"""

import requests
import sys

response_user = requests.get('https://jsonplaceholder.typicode.com/users')
response_todos = requests.get('https://jsonplaceholder.typicode.com/todos')
user = response_user.json()
todos = response_todos.json()

for item in user:
    if 'id' in item and str(item['id']) == str(sys.argv[1]):
            n = item['id']
n -= 1

i = 0
j = 0
l =[]
for item in todos:
      if 'userId' in item and str(item['userId']) == str(sys.argv[1]):
            if item['completed'] is True:
                  i += 1
                  l.append(item['title'])
            else:
                  j += 1

EMPLOYEE_NAME = user[n]['name']
NUMBER_OF_DONE_TASKS = i
TOTAL_NUMBER_OF_TASKS = i + j
print(f'Employee {EMPLOYEE_NAME} is done with tasks({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):')
for i in l:
      print('\t ' + i)
