from django.shortcuts import render

tasks = ['foo', 'bar']

# this view renders some predefined tasks
def index(request):
    # Query the to-do table and get all the records
    # tasks = Tasks.objects.all()
    context = {'tasks': tasks}
    return render(request, 'tasks/index.html', context)


def add(request):
    # determine if the user is submitting a task via the form or just viewing the add task page
    # if the user is just viewing the add task page, else statement will render add.html page
    if request.method == 'POST':
        # get the entered task from the request
        task = request.POST.get('task')
        # add the task to the to-do table
        # Todo.objects.create(task=task) # from models
        tasks.append(task)
        # redirect to index page
        # return redirect('index') # from models
        return render(request, 'tasks/index.html', context = {'tasks': tasks})

    else:
        return render(request, 'tasks/add.html')
