import requests
from pprint import pprint

URL = "http://127.0.0.1:5000/tasks"

def update_tasks(summary, description, task_id):
    update_tasks={
        "summary": summary,
        "description": description,
    }
    url = "%s/%s" % (URL, task_id)
    response = requests.put(url, json=update_tasks)
    if response.status_code == 204: 
        print("Task updated successfully.")
    else:
        print("Task creation failed.")

if __name__ == "__main__":
    print("Task updated successfully")
    summary = input("Summary:")
    description = input ("Description: ")
    update_tasks(summary, description)