from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import SoleoSerializer
from .models import SoleoDetails

# Create your views here.
@api_view(['GET', 'POST'])
def soleo_list(request):
    """

    Using one view point to handle 
    GET and POST request

    """
    if request.method == 'GET':
        details = SoleoDetails.objects.all()
        serializer = SoleoSerializer(details, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SoleoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=401)
    return Response()

@api_view(['GET', 'DELETE'])
def soleo_details(request, pk):
    """

    Using one view poin to handle
    Retrieve and Delete
        
    """
    
    try:
        detail = SoleoDetails.objects.get(pk=pk)
    except SoleoDetails.DoesNotExist:
        return Response(status=400)
        
    
    if request.method == 'GET':
        serializer = SoleoSerializer(detail)
        return Response(serializer.data, status=201)
    elif request.method == 'DELETE':
        detail.delete()
        return Response(status=201)
    