import data_manager
import click

@click.group()
def cli():
    pass



@cli.command()
@click.option('--title',required=True,help='Task title')
@click.option('--description',required=True,help='Task description')
@click.pass_context
def new(contexto,title,description):
    if not title or not description:
        contexto.fail('Title and description are required')
    else:
        data = data_manager.read()
        new_id= len(data) + 1
        new_task={
            "id":new_id,
            "title":title,
            "description":description
        }
        data.append(new_task)
        data_manager.write(data)
        print(f"Task {title} created successfully with id {new_id}")    

@cli.command()
def task():
    data = data_manager.read()
    for task in data:
        print(f"{task['id']} - {task['title']} - {task['description']}")

@cli.command()
@click.argument('id',type=int)
@click.option("--title",help="Task title")
@click.option("--description",help="Task description")
def update(id,title,description):
    data = data_manager.read()
    for task in data:
        if(task['id'] == id):
            if task is not None:
                task['title'] = title
            if description is not None:
                task['description'] = description
            else:
                print(f"Task with {id} not found")    
    data_manager.write(data)
    print(f"Task with id: {id} has been updated successfully")

@cli.command()
@click.argument("id",type=int)
def findTask(id):
    data = data_manager.read()
    task = next((x for x in data if x['id'] == id),None)
    if task is None:
        print(f"Task with id: {id} not found")
    else:
        print(f"Task: {task['title']} - {task['description']}")


@cli.command()
@click.argument("id",type=int)
def delete(id):
    data = data_manager.read()
    task = next((x for x in data if x['id'] == id),None)
    if task is None:
        print(f"Task with id: {id} not found")
    else:
        data.remove(task)
        data_manager.write(data)
        print(f"Task deleted successfully")


if __name__ == "__main__":
    cli()