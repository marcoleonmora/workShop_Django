from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'email', 'password']
        
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Correo E',
            'password': 'Contraseña',
        }
        
   