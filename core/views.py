from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

class ApiMsg(APIView):

    def get(self,request):
        return Response({"Message":"Olá Mundo"},status.HTTP_200_OK)
# Create your views here.
