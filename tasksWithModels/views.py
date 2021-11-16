from django.shortcuts import render, redirect
from tasksWithModels.models import TasksWithModels


# this view renders some predefined tasks
def index(request):
    # Query the to-do table and get all the records
    tasks = TasksWithModels.objects.all()
    context = {'tasks': tasks}
    return render(request, 'tasksWithModels/index.html', context)


def add(request):
    # determine if the user is submitting a task via the form or just viewing the add task page
    # if the user is just viewing the add task page, else statement will render add.html page
    if request.method == 'POST':
        # get the entered task from the request
        task = request.POST.get('task')
        # add the task to the to-do table
        TasksWithModels.objects.create(task=task)
        # redirect to index page
        return redirect('index')
    else:
        return render(request, 'tasksWithModels/add.html')