from django import forms
from .models import Infraestructura, Reserva, Deporte, Usuario
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth.models import User

class InfraestructuraForm(forms.ModelForm):
    class Meta:
        model = Infraestructura
        fields = ['nombre', 'tipo', 'capacidad', 'descripcion', 'horarios', 'precio']

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['deporte', 'infraestructura', 'fecha', 'horario']

class DeporteForm(forms.ModelForm):
    class Meta:
        model = Deporte
        fields = ['nombre', 'logo', 'slug']

class LoginForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=100)
    clave = forms.CharField(label='Clave', max_length=45, widget=forms.PasswordInput)
