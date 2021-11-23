from django.shortcuts import render
from .models import ToDoList
from django.http import HttpResponseRedirect

#Главная страница
def todoappView(request):
    all_todo_items = ToDoList.objects.all()
    return render(request, 'todoapp/index.html', {'all_items': all_todo_items})

#Обработка добавления задачи
def addToDoView(request):
    content_text = request.POST['content']
    new_item = ToDoList(content=content_text)
    new_item.save()
    return HttpResponseRedirect('/')

#Удаление задачи
def deleteTodoView(request, i):
    deleteapp = ToDoList.objects.get(id= i)
    deleteapp.delete()
    return HttpResponseRedirect('/')