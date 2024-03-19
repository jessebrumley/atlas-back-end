#!/usr/bin/python3

"""Script using REST API to fetch user name and todo list and export to CSV."""
import csv
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
    """Fetches list of employees by ID and returns
    a list of tasks with their completion status."""
    url = "https://jsonplaceholder.typicode.com/todos/"
    response = requests.get(url, params={'userId': employee_id})
    if response.status_code == 200:
        todo_list = response.json()
        tasks = []
        for task in todo_list:
            tasks.append({"title": task["title"],
                          "completed": task["completed"]})
        return tasks
    return []


def export_to_csv(employee_id, name, tasks):
    """Exports the task data to a CSV file."""
    filename = f"{employee_id}.csv"
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ["USER_ID", "USERNAME",
                      "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for task in tasks:
            writer.writerow({"USER_ID": employee_id, "USERNAME": name,
                             "TASK_COMPLETED_STATUS": "Completed"
                             if task["completed"] else "Incomplete",
                             "TASK_TITLE": task["title"]})


def get_employee_todo(employee_id):
    """Fetches a user's total, completed, and titles
    of a todo list by ID and exports to CSV."""
    name = get_name(employee_id)
    tasks = get_todos(employee_id)
    print(f"Employee {name} has {len(tasks)} tasks:")
    for task in tasks:
        print(f"\t {task['title']} - "
              f"{'Completed' if task['completed'] else 'Incomplete'}")
    export_to_csv(employee_id, name, tasks)


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    get_employee_todo(employee_id)
