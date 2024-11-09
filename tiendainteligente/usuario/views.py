from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistroUsuarioForm
from .models import Perfil
from django.contrib.auth.decorators import login_required

def registro(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()  # Guarda el usuario
            login(request, user)
            return redirect("crear_avatar")
    else:
        form = RegistroUsuarioForm()
    return render(request, "usuarios/registro.html", {"form": form})

def iniciar_sesion(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("crear_avatar")
    else:
        form = AuthenticationForm()
    return render(request, "usuarios/iniciar_sesion.html", {"form": form})

@login_required
def cerrar_sesion(request):
    logout(request)
    return redirect("iniciar_sesion")
