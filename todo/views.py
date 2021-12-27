from django.shortcuts import redirect, render, HttpResponse, get_object_or_404
from .models import Task
from .forms import TaskForm

# Create your views here.
def hello(request):
    tasks_list = Task.objects.all()
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    tasks = {'tasks': tasks_list, 'form': form}
    print(tasks['tasks'])
    print([task for task in tasks['tasks']])
    return render(request, 'tasks.html', context=tasks)


def updatetask(request, pk):
    obj = Task.objects.get(id=pk)
    form = TaskForm(instance=obj)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request,'update_task.html', context)