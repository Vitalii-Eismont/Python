from django.shortcuts import render, get_object_or_404
from .models import Task
from cart.form import CartAddTaskForm

def index(request):
    tasks = Task.objects.all()
    return render(request, 'main/index.html', {'title': 'Golovna storinka saity', 'tasks': tasks})

def about(request):
    return render(request, 'main/about.html', {'title': 'Сторінка про магазин'})

def task_detail(request, id, slug):
    task = get_object_or_404(Task, id=id, slug=slug, available=True)
    cart_task_form = CartAddTaskFormForm
    return render(request, 'cart/detail.html', {'task': task, 'cart_task_form': cart_task_form})