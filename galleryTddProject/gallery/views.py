from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from .models import Image, Usuario
import json

# Create your views here.
@csrf_exempt
def index(request):
    images_list = Image.objects.all()
    return HttpResponse(serializers.serialize("json", images_list))

@csrf_exempt
def add_user_view(request):
    if request.method == 'POST':
        json_user = json.loads(request.body)
        newUsuario = Usuario(
            username=json_user['username'],
            password = json_user['password'],
            name = json_user['name'],
            lastname = json_user['lastname'],
            email = json_user['email'],
            photo = json_user['photo'],
            educationLevel = json_user['educationLevel'],
            profession = json_user['profession'])
        newUsuario.save()

    return HttpResponse(serializers.serialize("json", [newUsuario]))

@csrf_exempt
def portfolio_public_view(request, id):

        portfolio_list = Image.objects.filter(user=id, profile='publ')
        return HttpResponse(serializers.serialize("json", portfolio_list))

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        jsonUser = json.loads(request.body)
        username = jsonUser['username']
        password = jsonUser['password']
        usuario = Usuario.objects.filter(username=username, password=password).first()
        if usuario is not None:
            message = username
        else:
            message = \
                'FAIL'

    return JsonResponse(message, safe=False)

@csrf_exempt
def edit_user(request):
    if request.method == 'POST':
        json_usuario = json.loads(request.body)
        user_edit = Usuario.objects.get(username=json_usuario['username'])
        user_edit.password = json_usuario['password']
        user_edit.name = json_usuario['name']
        user_edit.lastname = json_usuario['lastname']
        user_edit.email = json_usuario['email']
        user_edit.photo = json_usuario['photo']
        user_edit.educationLevel = json_usuario['educationLevel']
        user_edit.profession = json_usuario['profession']
        user_edit.save()
        return HttpResponse(serializers.serialize("json", [user_edit]))