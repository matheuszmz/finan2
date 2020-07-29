from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User


class DateInput(forms.DateInput):
    input_type = 'date'


class UserCreationForm(UserCreationForm):
    birthday = forms.DateField(widget=DateInput(), label='Data de Aniversário')
    email = forms.EmailField(label='Email')

    class Meta:
        model = User
        fields = ('name', 'birthday', 'cellphone', 'username', 'email', 'password1', 'password2')
