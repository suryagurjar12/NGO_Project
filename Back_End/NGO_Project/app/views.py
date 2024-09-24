from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse,HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.views import APIView
from .models import *
from .serializers import *
import io
from rest_framework import status 
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication


# Create your views here.
class SuperAdminViewSet(viewsets.ViewSet):
    
    def list(self, request):
        stu = SuperAdminModel.objects.all()
        serializer = SuperAdminSerializer(stu, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        id = pk
        if id is not None:
            stu = SuperAdminModel.objects.get(id=id)
            serializer = SuperAdminSerializer(stu)
            return Response(serializer.data)

    def create(self, request):
        serializer = SuperAdminSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self,request, pk):
        id = pk
        stu = SuperAdminModel.objects.get(pk=id)
        serializer = SuperAdminSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self,request, pk):
        id = pk
        stu = SuperAdminModel.objects.get(pk=id)
        serializer = SuperAdminSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Data Updated'})
        return Response(serializer.errors)

    def destroy(self,request, pk):
        id = pk
        stu = SuperAdminModel.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data Deleted'})


class MovieViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = SuperAdminModel.objects.all()
    serializer_class = SuperAdminSerializer





# class Studentviewset(viewsets.ModelViewSet):
#     queryset = SpuerAdminModel.objects.all()
#     serializer_class = StudentSerializer
