from urllib import request
from winreg import QueryValue
from django.http import HttpResponse
# from django.shortcuts import render
# from rest_framework.decorators import api_view

# from .models import *
# @api_view(['POST'])
# def post(request):
#        nums = eval(request.body.decode('utf-8'))
#        num1 = int(nums["number_1"])
#        num2 = int(nums["number_2"])
#        return HttpResponse(str(num1 + num2))

from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *

class listtodo(generics.CreateAPIView):
    queryset=calc.objects.all()
    serializer_class=calsSerializer


# class read(generics.ListAPIView):
#     queryset=calc.objects.all()
#     serializer_class=calsSerializer
