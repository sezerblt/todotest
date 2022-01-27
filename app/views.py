import re
from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import TodoModel
from .forms import TodoForm,UpdateTodoForm

# Create your views here.

def index1(request):
    todos = TodoModel.objects.all()
    count_todos = todos.count()

    completed_todo = TodoModel.objects.filter(complete=True)
    count_completed_todo = completed_todo.count()

    uncompleted = count_todos - count_completed_todo


    context = {
        'todos': todos,
        'count_todos': count_todos,
        'count_completed_todo': count_completed_todo,
        'uncompleted': uncompleted,
    }
    return render(request, 'app/index.html', context)

def create(request):
    todos = TodoModel.objects.all()
    count_todos = todos.count()
    completed_todo = TodoModel.objects.filter(complete=True)
    count_completed_todo = completed_todo.count()
    uncompleted = count_todos - count_completed_todo
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TodoForm()
    context = {
        'todos': todos,
        'form': form,
        'count_todos': count_todos,
        'count_completed_todo': count_completed_todo,
        'uncompleted': uncompleted,
    }

    return render(request, 'app/create.html', context)


def update(request, id):
    todo = TodoModel.objects.get(id=id)
    if request.method == 'POST':
        form = UpdateTodoForm(request.POST, instance=TodoModel.objects.get(id=id))
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UpdateTodoForm(instance=TodoModel.objects.get(id=id))
    context = {
        'form': form
    }
    return render(request, 'app/update.html', context)


def delete(request, id):
    todo = TodoModel.objects.get(id=id)
    if request.method == 'POST':
        todo.delete()
        return redirect('/')
    return render(request, 'app/delete.html')


def context(request,id):
    todo=TodoModel.objects.get(id=id)
    context_todo={
        "todo":todo
    }
    return render(request,'app/context.html',context_todo)