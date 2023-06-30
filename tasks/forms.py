from django import forms
from .models import Project
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','password1','password2']
    

class AgendarForm(forms.ModelForm):
    
    nombre = forms.CharField( label="Nombre", required=True, widget=forms.TextInput(attrs= {'class': 'form-control'}))
    apaterno = forms.CharField( label= "Apellido paterno", required=True, widget=forms.TextInput(attrs= {'class': 'form-control'}))
    amaterno = forms.CharField( label= "Apellido materno", required=True, widget=forms.TextInput(attrs= {'class': 'form-control'}))
    correo = forms.EmailField( label= "Correo", required=True, widget=forms.EmailInput(attrs= {'class': 'form-control' ,'placeholder':'nombre@ejemplo.cl'}))
    hora = forms.DateTimeField( label="Elige Horario", required=True, widget=forms.DateTimeInput(attrs= {'class': 'form-control' ,'type':'datetime-local' }))
    comentario = forms.CharField( label= "Comentario", widget=forms.Textarea(attrs= {'class': 'form-control', 'rows':3, 'placeholder': 'Escribe algun comentario que debamos saber'}))

    class Meta:
        model = Project
        fields = '__all__'