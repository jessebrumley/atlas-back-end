#!/usr/bin/python3

"""Script using REST API to fetch user name and todo list."""
import json
import requests
import sys


def get_name(employee_id):
    """Fetches the name of the employee by ID."""
    url = "https://jsonplaceholder.typicode.com/users/"
    response = requests.get(url, params={'id': employee_id})
    if response.status_code == 200:
        users = response.json()
        for user in users:
            if user['id'] == employee_id:
                return user.get('name', 'No name found')
    return ('Failed to fetch name')


def get_todos(employee_id):
    """Fetches list of employees by ID."""
    url = "https://jsonplaceholder.typicode.com/todos/"
    response = requests.get(url, params={'userId': employee_id})
    if response.status_code == 200:
        todo_list = response.json()
        tasks = []
        for task in todo_list:
            tasks.append({
                "task": task["title"],
                "completed": task["completed"],
                "username": get_name(employee_id)
            })
        return tasks
    return []


def get_employee_todo(employee_id):
    """Fetches a user's total, completed, and titles of a todo list by ID."""
    tasks = get_todos(employee_id)
    if tasks:
        data = {str(employee_id): tasks}
        with open(f"{employee_id}.json", "w") as outfile:
            json.dump(data, outfile, indent=None)


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    get_employee_todo(employee_id)
