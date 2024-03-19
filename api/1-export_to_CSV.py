#!/usr/bin/python3

"""Script using REST API to fetch user name and todo list and export to CSV."""
import requests
import sys
import csv

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
        completed_tasks = []
        for task in todo_list:
            if task["completed"]:
                completed_tasks.append(task["title"])
        total_done = len(completed_tasks)
        total_todo = len(todo_list)

        return (total_done, total_todo, completed_tasks)
    return []

def export_to_csv(employee_id, name, completed_tasks):
    """Exports the task data to a CSV file."""
    filename = f"{employee_id}.csv"
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for task in completed_tasks:
            writer.writerow({"USER_ID": employee_id, "USERNAME": name, "TASK_COMPLETED_STATUS": "Completed", "TASK_TITLE": task})

def get_employee_todo(employee_id):
    """Fetches a user's total, completed, and titles of a todo list by ID and exports to CSV."""
    name = get_name(employee_id)
    todos = get_todos(employee_id)
    print(
        f"Employee {name} is done with tasks("
        f"{todos[0]}/{todos[1]}):"
        )
    completed_tasks = todos[2]
    for completed_task in completed_tasks:
        print(f"\t {completed_task}")
    export_to_csv(employee_id, name, completed_tasks)

if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    get_employee_todo(employee_id)
