from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django import forms

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(label='Email')
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = (
            "username",
            "email",
            "password1",
            "password2",
        )

class CustomUserChangeForm(UserChangeForm):
    email = forms.EmailField(label='Email')

    class Meta:
        model = CustomUser
        fields = (
            "username",
            "email",
            "preferred_contact",
        )
