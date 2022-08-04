from django.urls import path
from home.views import apiOverview, taskList, taskDetail, taskCreate, taskUpdate, taskDelete

urlpatterns = [
    path('', apiOverview, name="apiOverview"),
    path('task-list/', taskList, name="taskList"),
    path('task-create/', taskCreate, name="taskCreate"),


    path('task-detail/<str:pk>/', taskDetail, name="taskDetail"), 

    path('task-update/<str:pk>/', taskUpdate, name="taskUpdate"),

     path('task-delete/<str:pk>/',   taskDelete, name="taskDelete")



]