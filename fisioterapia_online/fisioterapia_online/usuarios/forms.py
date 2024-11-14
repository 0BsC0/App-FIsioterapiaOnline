from django import forms
from .models import Perfil  
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class UserProfileForm(forms.ModelForm):
    first_name = forms.CharField(label="Nombres", max_length=30, required=True)
    last_name = forms.CharField(label="Apellidos", max_length=30, required=True)
    
    class Meta:
        model = Perfil
        fields = [
            "first_name", "last_name", "identificacion", "telefono", "fecha_nacimiento", 
            "direccion", "historial_medico", "alergias", "medicacion_actual", 
            "objetivos", "ultima_cita", "nivel_actividad"
        ]
        widgets = {
            'fecha_nacimiento': forms.SelectDateWidget(years=range(1900, 2100)),
            'historial_medico': forms.Textarea(attrs={'rows': 3}),
            'objetivos': forms.Textarea(attrs={'rows': 3}),
        }

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))

    class Meta:
        model = User  # Usa el modelo de usuario predeterminado de Django
        fields = ['username', 'email', 'password1', 'password2']


class IniciarSesionForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
