from django.shortcuts import render
from random import SystemRandom
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer
from .models import User
from rest_framework.response import Response
from django.contrib.auth import get_model_model
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login,logout
import re

def generate_session_token(length = 10):
    return ''.join([SystemRandom().choice([chr(i) for i in range(97,123)] + [str(i) for i in range(10)]) for _ in range(length)])

def signin(request):
    if request.Method == 'GET':
        return Response({'error': ' send a post request with appropriate values'})

    username = request.POST['email']
    password = request.POST['password']

    if not re.match('^((?!\.)[\w-_.]*[^.])(@\w+)(\.\w+(\.\w+)?[^.\W])',username):
        return Response({'error': 'email sahi de daal bhai'})