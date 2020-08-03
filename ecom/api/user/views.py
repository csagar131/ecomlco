from django.shortcuts import render
from random import SystemRandom
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer
from .models import User
from django.http import JsonResponse
from django.contrib.auth import get_user_model, login, logout
from django.views.decorators.csrf import csrf_exempt
import re


def generate_session_token(length=10):
    return ''.join([SystemRandom().choice([chr(i) for i in range(97, 123)] + [str(i) for i in range(10)]) for _ in range(length)])


@csrf_exempt
def signin(request):
    if not request.method == 'POST':
        return JsonResponse({'error': ' send a post request with appropriate values'})

    username = request.POST['email']
    password = request.POST['password']

    # validation part
    if not re.match('[\w\.-]+@[\w\.-]+\.\w{2,4}', username):
        return JsonResponse({'error': 'please provide correct email address'})

    UserModel = get_user_model()

    try:
        user = UserModel.objects.get(email=username)
        if user.check_password(password):
            usr_dict = UserModel.objects.filter(
                email=username).values().first()
            usr_dict.pop('password')

            if user.session_token != '0':
                user.session_token = '0'
                user.save()
                return JsonResponse({'error': 'previous session exist'})

            token = generate_session_token()
            user.session_token = token
            user.save()
            login(request, user)
            return JsonResponse({'token': token, 'user': usr_dict})
        return JsonResponse({'error': 'Invalid password'})
    except UserModel.DoesNotExist:
        return JsonResponse({'error': 'Invalid Email'})

@csrf_exempt
def signout(request, id):
    UserModel = get_user_model()
    try:
        user = UserModel.objects.get(id=id)
        user.session_token = '0'
        user.save()
    except UserModel.DoesNotExist:
        return JsonResponse({'error': 'Invalid Id'})
    logout(request)
    return JsonResponse({'success': 'logged out succefully'})


class UserViewSet(viewsets.ModelViewSet):
    permission_classes_by_action = {
        'create': [AllowAny],
    }
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        try:
            # return permission_classes depending on `action`
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes_by_action]
