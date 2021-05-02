from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'hello/index.html', {'title': 'hello', 'tasks': tasks})


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'From is not right'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'hello/create.html', context)
