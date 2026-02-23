#!/usr/bin/python3

""" To-do List Progress Reporter
Fetches data and displays To-list progress for a given ID. """

import requests

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
    employee_id = input("Enter the Employee ID: ")
    show_progress(employee_id)
    