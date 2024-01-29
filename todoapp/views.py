from django.shortcuts import render, redirect

from todoapp.forms import TodoForm
from .models import Todo

# Create your views here.
def index(request):
    todos = Todo.objects.all()

    # Handle search
    search_query = request.GET.get('search', '')
    if search_query:
        todos = todos.filter(title__icontains=search_query)

    if request.method == 'POST':
        new_todo = Todo(title=request.POST['title'])
        new_todo.save()
        return redirect('/')

    return render(request, 'index.html', {'todos': todos, 'search_query': search_query})

def delete(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return redirect('/')

def edit(request, pk):
    todo = Todo.objects.get(id=pk)

    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)

        if form.is_valid():
            form.save()

            return redirect('home')
    else:
        form = TodoForm(instance=todo)

    return render(request, 'edit_task.html', {'form': form , 'todo' : todo})

def loginPage(request):
    return render(request, 'login&Signup.html')

def registerPage(request):
    return render(request, 'login&Signup.html')