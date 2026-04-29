from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Correo electrónico") # Añade el label aquí

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name"]
        # También puedes traducir las etiquetas de los campos del modelo User así:
        labels = {
            'username': 'Nombre de usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
        }