from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms


class CustomAuthenticationForm(AuthenticationForm):
    error_messages = {
        'invalid_login': "Usuario o contraseña incorrectos. Inténtalo de nuevo.",
        'inactive': "Esta cuenta está deshabilitada.",
    }

class Registro(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Obligatorio. Ingrese un email válido.")
    password1 = forms.CharField(label="Contrasenia", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contrasenia", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']  
        help_texts = {
            'username': '',
            'email': '',
            'password1': '',
            'password2': '',
        }
        
class EditarPerfil(UserChangeForm):
    password= None
    email= forms.EmailField()
    first_name= forms.CharField(label="Nombre")
    last_name= forms.CharField(label="Apellido")
    
    class Meta:
        model=User
        fields = ['email', 'first_name', 'last_name']
        help_texts = {llave : '' for llave in fields}