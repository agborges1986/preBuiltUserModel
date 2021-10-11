from django.shortcuts import render
from .forms import *
# Create your views here.
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

import random


def register(request):
    form = AuthenticationForm
    form2 = UserCreateForm(request.POST)
    print(form2.is_valid())
    if form2.is_valid():
        user = form2.save(commit=False) # commit = False crea un nuevo objeto de usuario que aún no está en la base de datos.
        user.save() # si no tenemos nada más que necesitemos hacer con el usuario
    print(form2.errors)
    return render(request, "index.html", {"form":form(), "form2":form2})

def home(request):
    testuser=authenticate(username=request.POST['username'], password=request.POST['password'])
    login(request,testuser)
    print(request.user.first_name)
    users = User.objects.all() #retrieves all users
    print(request.user)
    return render(request, 'home.html', {'users': users, 'active':request.user})


def index(request):
    form = AuthenticationForm
    #User.objects.create_user(first_name="Mike", last_name="Hannon", username=str(random.randint(0,100)))
    # Crea una cadena aleatoria como un nombre de usuario arbitrario. ya que son únicos
    users = User.objects.all() #retrieves all users
    return render(request, 'index.html', {'form': form()})


# Dentro de views.py de su aplicación
from django.shortcuts import render, redirect
from .forms import RegisterForm

def indexForm(request):
    form = UserCreateForm()
    context = { "regForm": form }
    return render(request, "indexForm.html", context)
