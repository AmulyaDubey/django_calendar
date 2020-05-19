from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from .models import Event
from datetime import datetime

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=150, help_text='Email')


    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class LoginForm(forms.Form):
    email = forms.EmailField(max_length=150)
    password=forms.CharField(max_length=150 )
    
    class Meta:
        model = User
        fields = ('email', 'password')

class newEvent(forms.Form):
    title=forms.CharField(max_length=100)
    date=forms.DateField()

    class Meta:
        model= Event
        feilds=('title','date')

class searchEvent(forms.Form):
    title=forms.CharField(max_length=100)

    class Meta:
        model= Event
        feilds=('title')

