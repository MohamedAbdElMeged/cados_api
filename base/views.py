from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Advocate
from .serializers import AdvocateSerializer

# Create your views here.
@api_view(['GET'])
def endpoints(request):
    data = ['/advocates','/advocates/:username']
    return Response(data)

@api_view(['GET'])
def advocates_list(request):
    query = request.GET.get('query')
    if query == None:
        query = ''
    advocates = Advocate.objects.filter(username__icontains= query)
    advocates_serilaized = AdvocateSerializer(advocates,many=True)
    return Response(advocates_serilaized.data)

@api_view(['GET'])
def advocate_detail(request,username):
    advocate = Advocate.objects.get(username=username)
    advocate_serilaized = AdvocateSerializer(advocate,many=False)
    return Response(advocate_serilaized.data,status=status.HTTP_200_OK)