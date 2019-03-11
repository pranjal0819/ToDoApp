from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import TodoData
from .serializers import TodoSerializer


# Create your views here.

class ToDoList(APIView):

    def get(self, request, email):
        todo_list = TodoData.objects.filter(email=email)
        dictionaries = [obj.as_dict() for obj in todo_list]
        # serializer = TodoSerializer(todo_list, many=True)
        return Response(dictionaries)

    def post(self, request, email):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TodoDetail(APIView):
    def get_object(self, request, email, pk):
        try:
            return TodoData.objects.get(email=email, pk=pk)
        except TodoData.DoesNotExist:
            raise Http404

    def get(self, request, email, pk):
        obj = self.get_object(request, email, pk)
        dictionaries = [obj.as_dict()]
        # serializer = TodoSerializer(obj)
        return Response(dictionaries)

    def put(self, request, email, pk, format=None):
        obj = self.get_object(request, email, pk)
        serializer = TodoSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            dictionaries = [obj.as_dict()]
            return Response(dictionaries)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, email, pk, format=None):
        obj = self.get_object(request, email, pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
