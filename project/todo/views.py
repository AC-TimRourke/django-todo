from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.urls import reverse

from .models import Todo

# Create your views here.
def index(request):
    all_todos = Todo.objects.order_by('-created_at')
    template = loader.get_template('todos/index.html')
    context = {
        'all_todos': all_todos,
    }
    return HttpResponse(template.render(context, request))

def todo(request, todo_id):
    try:
        todo = Todo.objects.get(pk=todo_id)
    except Todo.DoesNotExist:
        raise Http404("Todo with the ID %s does not exist." % todo_id)
    return render(request, 'todos/todo.html', {'todo': todo})

def update(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    try:
        todo.update_description(description)
        todo.save()
        return HttpResponseRedirect(reverse('todos:todo', args=(todo.id,)))
    except(KeyError):
        return render(request, 'todos/todo.html', {
            'todo': todo,
            'error_message': 'You did not provide a description.'
        })

def create(request):
    try:
        new_todo = Todo.create(request.POST['description'])
        return HttpResponseRedirect(reverse('todos:index'))
    except KeyError:
        return render(request, 'todos/index.html', {
            'error_message': 'You did not provide a description.'  
        })