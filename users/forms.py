from django.contrib.auth.forms import UserCreationForm
from core.models.user import User
from .models import Profile
from django import forms


class CustomUserCreationForm(UserCreationForm):
    """This class represents the user register form.
    """

    class Meta(UserCreationForm):
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Le nom d'utilisateur existe déjà")
        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("L'emai existe déjà")
        return email


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'email')


class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['image']
