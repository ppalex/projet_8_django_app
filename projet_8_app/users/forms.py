from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from core.models.user import User


class CustomUserCreationForm(UserCreationForm):
    

    class Meta(UserCreationForm):
        model = User
        fields = ('username','password1', 'password2')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('email',)