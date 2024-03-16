#!/usr/bin/python3
""" Script using REST API """
import requests
import sys


def get_employee_todo(employee_id):
    """
    Retrieves and displays the TODO list of an employee using a REST API.

    Parameters:
    - employee_id: int
        The ID of the employee for whom the TODO list is to be retrieved.
    """

    # Setting API paths
    url = "https://jsonplaceholder.typicode.com/"
    user_ext = f"{url}/users/{employee_id}]"
    todo_ext = f"{url}/todos"

    # Sending a GET request to the API endpoint
    employee_info = requests.get(user_ext).json()
    employee_name = employee_info.get('name')
    todo_list = requests.get(f"{todo_ext}?userId={user_ext}").json()

    # Counting the number of completed tasks
    completed_tasks = []
    for task in todo_list:
        if task["completed"]:
            completed_tasks.append(task["title"])

    # Counting the totals of tasks and tasks done
    total_todo = len(todo_list)
    total_done = len(completed_tasks)

    # Displaying the employee TODO list progress
    print(
        f"Employee {employee_name} is done with tasks("
        f"{total_done}/{total_todo}):"
        )

    # Displaying the titles of completed tasks
    for completed_task in completed_tasks:
        print(f"\t {completed_task}")


if __name__ == "__main__":
    pass
