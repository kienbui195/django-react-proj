from django.shortcuts import render
from .models import Todo
from .serializers import TodoSerializer
from rest_framework import generics

# Create your views here.
class TodoViewList (generics.ListCreateAPIView):
  queryset = Todo.objects.all()
  serializer_class = TodoSerializer
  
class TodoDeleteView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Todo.objects.all()
  serializer_class = TodoSerializer
