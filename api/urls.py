from django.urls import path
from .views import TodoViewList, TodoDeleteView

urlpatterns = [
    path('todo', TodoViewList.as_view()),
    path('todo/edit/<int:pk>', TodoDeleteView.as_view()),
]
