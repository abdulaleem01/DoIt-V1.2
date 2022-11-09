from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . models import TcData
from . serializers import TcDataSerializer

@api_view(['GET'])
def getData(request):
    items = TcData.objects.all()
    serializer = TcDataSerializer(items,many = True)
    return Response(serializer.data)


@api_view(['GET'])
def getDatasingle(request,pk):
    items = TcData.objects.get(pk = pk)
    serializer = TcDataSerializer(items)
    return Response(serializer.data)

@api_view(['POST'])
def postData(request):
    serializer = TcDataSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)