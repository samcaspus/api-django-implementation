from rest_framework import viewsets
from .serializers import JobSerializer
from .models import JobsList
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response



@api_view(['GET', 'POST'])
def jobsView(request):
    if request.method == 'GET':
        viewJobs = JobsList.objects.all()
        serializer = JobSerializer(viewJobs, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = JobSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)