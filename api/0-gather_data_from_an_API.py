#!/usr/bin/python3

""" To-do List Progress Reporter
Fetches data and displays To-list progress for a given ID. """

import requests
import sys


API_URL = "https://jsonplaceholder.typicode.com"


def get_employee_data(employee_id):
    response = requests.get(f"{API_URL}/users/{employee_id}")
    response.raise_for_status()
    return response.json()


def get_todos(employee_id):
    response = requests.get(f"{API_URL}/todos?userId={employee_id}")
    response.raise_for_status()
    return response.json()


def show_progress(employee_id):
    try:
        employee = get_employee_data(employee_id)
    except:
        print(f'Error: Employee with the ID {employee_id} was not found.')
      
    todos = get_todos(employee_id)
    
    if not todos:
        print(f'The employee with the ID {employee_id} has no tasks on their To-do list.')
        
    total_tasks = len(todos)
    completed_tasks = [task for task in todos if task['completed']]
    
    num_completed = len(completed_tasks)

    print(f"Employee {employee['name']} is done with tasks({num_completed}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task['title']}")
    
    
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)
        
    try:
        employee_id = int(sys.argv[1])
        if employee_id <= 0:
            raise ValueError
    except ValueError:
        print("Error: Employee ID must be a positive Integer.")
        sys.exit(1)
        
    show_progress(employee_id)
    