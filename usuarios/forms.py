from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Avatar


class RegisterForm(UserCreationForm):
    usable_password = None

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        # fields = "__all__"


class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['imagen']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name"]
