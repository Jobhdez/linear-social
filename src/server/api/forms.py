from django import forms 
from .models import LinearAlgebraExpression
from django.contrib.auth import get_user_model
User = get_user_model()

"""Module that corresponds the forms that get used in the `views.py` module."""

class UserRegistrationForm(forms.ModelForm):
    """Form that enables the server receive the password, username, first_name
    and email of the given user that is registering."""
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class LoginForm(forms.Form):
    """Form that enables the server receive the username and password
    of the given user who is login in"""
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RequestFriendForm(forms.Form):
    
    id = forms.CharField()

class AcceptForm(forms.Form):
    id = forms.CharField()

class LinearAlgebraExpForm(forms.ModelForm):
    class Meta:
        model = LinearAlgebraExpression
        fields = ['exp']
