from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse
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