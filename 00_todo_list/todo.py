import click 
import json
import os

TODO_FILE = "todo.json" #file name

# upadate the task in todo.json file
def load_todo():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as file:
        return json.load(file)

 # save task to todo.json file   
def save_todo(tasks):
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# crate to add different features/command eg: add, list , complete, delete
@click.group()
def cli():
    """Simple to-do list Manager"""
    pass

# add task 📝
@click.command()
@click.argument("task")
def add(task):
    """Add a new task to the to-do list"""
    tasks = load_todo()
    tasks.append({"task":task, "done":False})
    save_todo(tasks)
    click.echo(f"200: '{task}' added to list.")

#show list of task 📃
@click.command()
def list():
    """List all tasks in the to-do list"""
    tasks = load_todo()
    if not tasks:
        click.echo("empty list 🪹")
        return
    for index, task in enumerate(tasks, 1):
        status = "✅" if task["done"] else "❌"
        click.echo(f"{index}. {task['task']} - [{status}]")

#complete task: feature for marking a task as complete ✅
@click.command()
@click.argument("task_number", type=int)
def complete (task_number):
    """Mark a task as complete"""
    tasks = load_todo()
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]["done"] = True
        save_todo(tasks)
        click.echo(f"{task_number}) mark as completed ✅")

    else:
        click.echo(f"Invalid task number, number of task {len(tasks)}")

#delete task 🗑️    
@click.command()
@click.argument("task_number", type=int)
def delete(task_number):
    """Delete a task from the to-do list"""
    tasks = load_todo()
    if 0 < task_number <= len(tasks):
        delete_task = tasks.pop(task_number - 1)
        save_todo(tasks)
        click.echo(f"{task_number} task deleted")
    else:
        click.echo(f"Invalid task number, number of task {len(tasks)}")

#add commands to the cli
cli.add_command(add)
cli.add_command(list)
cli.add_command(complete)
cli.add_command(delete)

if __name__ == "__main__":
    cli()
    