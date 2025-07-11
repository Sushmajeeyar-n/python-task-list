tasks = []

def add_task(task):
    tasks.append(task)

def view_tasks():
    for i, task in enumerate(tasks):
        print(f"{i+1}. {task}")

add_task("Learn GitHub")
add_task("Apply for jobs abroad")
view_tasks()
