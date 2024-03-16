#!/usr/bin/python3
""" This function connects to an API and retrieves data about an Employee """
import requests
import sys


def employee_todo_list(employee_id):
    """ This function displays an Employee's todo list progress """

    response = requests.get(
        'https://jsonplaceholder.typicode.com/users/{employee_id}'
    )

    if response.status_code == 200:
        """ Checks if the request is successful and parses the data """
        employee_data = response.json()

        EMPLOYEE_NAME = employee_data['name']
        tasks = employee_data['tasks']
        NUMBER_OF_DONE_TASKS = sum(1 for tasks in tasks if task['completed'])
        TOTAL_NUMBER_OF_TASKS = len(tasks)

        print(
            f"Employee {EMPLOYEE_NAME} is done with tasks("
            f"{NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):"
        )
    else:
        print("Failed to retrieve data")


if __name__ == "__main__":
    pass
