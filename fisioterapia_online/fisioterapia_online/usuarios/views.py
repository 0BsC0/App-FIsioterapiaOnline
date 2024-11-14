from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate
from usuarios.forms import UserProfileForm
from .forms import RegistroForm, IniciarSesionForm
from .models import Perfil


def salir(request):
    logout(request)
    return redirect('/')


@login_required
def user_profile(request):
    profile, created = Perfil.objects.get_or_create(user=request.user)
    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            # Guardar Nombres y Apellidos en el modelo User
            request.user.first_name = form.cleaned_data['first_name']
            request.user.last_name = form.cleaned_data['last_name']
            request.user.save()
            profile.save()
            messages.success(request, "Perfil actualizado correctamente.")
            return redirect('user_dashboard')
        else:
            messages.error(request, "Por favor, corrige los errores en el formulario.")
    else:
        form = UserProfileForm(instance=profile, initial={
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
        })
    return render(request, 'usuarios/profile.html', {'form': form})



def register(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')  # Redirige al dashboard después del registro
    else:
        form = RegistroForm()
    return render(request, 'registration/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = IniciarSesionForm(data=request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Autenticar al usuario
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirige al dashboard después del login
        else:
            # Si la autenticación falla, muestra un mensaje de error
            messages.error(request, "Usuario o contraseña incorrectos. Si no tienes una cuenta, regístrate.")
    else:
        form = IniciarSesionForm()
    return render(request, 'registration/login.html', {'form': form})


@login_required
def user_dashboard(request):
    return render(request, 'usuarios/dashboard.html')
