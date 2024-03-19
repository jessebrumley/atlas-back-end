#!/usr/bin/python3

"""Script using REST API to fetch user name and todo list."""
import json
import requests
import sys


def get_name(employee_id):
    url = "https://jsonplaceholder.typicode.com/users/"
    response = requests.get(url, params={'id': employee_id})
    if response.status_code == 200:
        users = response.json()
        for user in users:
            if user['id'] == employee_id:
                return user.get('name', 'No name found')
    return ('Failed to fetch name')


def get_todos(employee_id):
    url = "https://jsonplaceholder.typicode.com/todos/"
    response = requests.get(url, params={'userId': employee_id})
    if response.status_code == 200:
        todo_list = response.json()
        tasks = []
        for task in todo_list:
            tasks.append({
                "username": get_name(employee_id),
                "task": task["title"],
                "completed": task["completed"]
            })
        return tasks
    return []


def get_all_employees_todos():
    url = "https://jsonplaceholder.typicode.com/users/"
    response = requests.get(url)
    if response.status_code == 200:
        users = response.json()
        all_tasks = {}
        for user in users:
            user_id = str(user['id'])
            tasks = get_todos(user['id'])
            if tasks:
                all_tasks[user_id] = tasks
        return all_tasks
    return {}


def export_all_employees_todos():
    all_tasks = get_all_employees_todos()
    with open("todo_all_employees.json", "w") as outfile:
        json.dump(all_tasks, outfile, indent=None)


if __name__ == "__main__":
    export_all_employees_todos()
