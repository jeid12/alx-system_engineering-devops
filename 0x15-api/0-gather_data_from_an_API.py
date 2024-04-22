import requests
import sys

def get_todo_list_progress(employee_id):
    # URL for the API
    base_url = "https://jsonplaceholder.typicode.com"
    todos_url = f"{base_url}/todos?userId={employee_id}"
    
    # Fetching data from the API
    response = requests.get(todos_url)
    todos = response.json()
    
    # Counting completed and total tasks
    completed_tasks = [task for task in todos if task['completed']]
    total_tasks = len(todos)
    num_completed_tasks = len(completed_tasks)
    
    # Getting the employee's name
    user_url = f"{base_url}/users/{employee_id}"
    response = requests.get(user_url)
    user_data = response.json()
    employee_name = user_data['name']
    
    # Printing the progress
    print(f"Employee {employee_name} is done with tasks ({num_completed_tasks}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t{task['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)
        
    employee_id = int(sys.argv[1])
    get_todo_list_progress(employee_id)

