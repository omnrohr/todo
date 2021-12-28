from django.shortcuts import redirect, render
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

def deletetask(request, pk):
    obj = Task.objects.get(id=pk)
    if request.method=='POST':
        obj.delete()
        return redirect('tasks')
    context = {'task': obj}
    return render(request, 'delete.html', context)
    