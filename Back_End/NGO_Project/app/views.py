from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *


@api_view(['GET', 'POST']) 
def Registration(request):
    if request.method=='GET':
        user=RegistrationModel.objects.all()
        serializer=RegistrationSerializer(user,many=True)
        return Response(serializer.data)
    
    
    elif request.method=='POST':
        serializer=RegistrationSerializer(data=request.data) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data) 
        else: return Response(serializer.errors)
        
@api_view(['GET', 'POST']) 
def Admin(request):
    if request.method=='GET':
        user=AdminModel.objects.all()
        serializer=AdminSerializer(user,many=True)
        return Response(serializer.data)
    
    elif request.method=='POST':
        serializer=AdminSerializer(data=request.data) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data) 
        else: return Response(serializer.errors)