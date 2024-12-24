from .models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class CustomerUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your Username'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter your Email ID'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter you Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter you Password again'}))

    class Meta:
        model = User
        fields = ['username','email','password1','password2']