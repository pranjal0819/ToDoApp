from django.contrib import admin
from django.urls import path

from api.views import ToDoList, TodoDetail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo-api/<email>/list', ToDoList.as_view()),
    path('todo-api/<email>/detail/<int:pk>', TodoDetail.as_view()),
]
