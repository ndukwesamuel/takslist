from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response


from .models import Task
from .serializers import TaskSerializer

# Create your views here.


def home(request):

    return render(request, "index.html")


@api_view(['GET'])
def apiOverview(request):
    api_urls = {'List':'/task-list/',}
    return Response(api_urls)


@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    
    return Response(serializer.data)



@api_view(['GET'])
def taskDetail(request, pk ):
    tasks = Task.objects.get(id = pk)
    serializer = TaskSerializer(tasks, many=False)

    return Response(serializer.data)


@api_view(['POST'])
def taskCreate(request):
    serializerinfo = TaskSerializer(data= request.data)

    if serializerinfo.is_valid():
        serializerinfo.save()

    return Response(serializerinfo.data)



@api_view(['POST'])
def taskUpdate(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task,data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)




@api_view(['DELETE'])
def taskDelete(request, pk):

    task = Task.objects.get(id=pk)
    task.delete()
    return Response('Item succsesfully deleted ')

