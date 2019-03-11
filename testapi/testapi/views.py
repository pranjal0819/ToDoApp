import datetime

import requests
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import TemplateView


# Create your views here.
class DataList(TemplateView):

    def get(self, request, **kwargs):
        request.session['email'] = 'pranjal0819@gmail.com'
        url = str('http://localhost:8004/todo-api/' + request.session['email'] + '/list')
        todo = requests.get(url=url).json()
        return render(request, 'todo.html', {'todo_list': todo})


# noinspection PyBroadException
class DetailTodo(TemplateView):

    def get(self, request, *args, **kwargs):
        url = str('http://localhost:8004/todo-api/' + request.session['email'] + '/detail/' + kwargs['id'])
        todo = requests.get(url=url).json()
        return render(request, 'todo-detail.html', {'todo': todo[0]})

    def post(self, request, **kwargs):
        title = request.POST['title']
        message = request.POST['message']
        time = str(datetime.datetime.strptime(request.POST['time'], '%d %b %Y %H:%M:%S'))
        try:
            d = request.POST['complete']
            complete = True
        except Exception:
            complete = False
        url = str('http://localhost:8004/todo-api/' + request.session['email'] + '/detail/' + kwargs['id'])
        data = {"title": title, "message": message, "email": request.session['email'], "time": time,
                "complete": complete}
        todo = requests.put(url=url, data=data)
        if todo.status_code == 200:
            messages.success(request, 'ToDO update')
            return redirect('/')
        messages.error(request, 'Invalid Input')
        return render(request, 'todo-detail.html', {'todo': todo})


# noinspection PyBroadException
class AddTodo(TemplateView):

    def get(self, request, *args, **kwargs):
        return render(request, 'todo-detail.html')

    def post(self, request):
        title = request.POST['title']
        message = request.POST['message']
        time = str(datetime.datetime.strptime(request.POST['time'], '%d %b %Y %H:%M:%S'))
        try:
            d = request.POST['complete']
            complete = True
        except Exception:
            complete = False
        url = str('http://localhost:8004/todo-api/' + request.session['email'] + '/list')
        data = {"title": title, "message": message, "email": request.session['email'], "complete": complete,
                "time": time}
        todo = requests.post(url=url, data=data)
        if todo.status_code == 201:
            messages.success(request, 'ToDO added to your List')
            return redirect('/')
        messages.error(request, 'Invalid Input')
        return render(request, 'todo-detail.html', {'todo': todo})


class DeleteToDo(TemplateView):
    def get(self, request, *args, **kwargs):
        url = str('http://localhost:8004/todo-api/' + request.session['email'] + '/detail/' + kwargs['id'])
        todo = requests.delete(url)
        if todo.status_code == 204:
            messages.success(request, 'Successfully Deleted Todo')
            return redirect('/')
        messages.error(request, 'Invalid Request')
        return redirect('/')
