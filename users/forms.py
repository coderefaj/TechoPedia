from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username','team_name', 'email','college','phone_no')
        labels = {
            "username" :"Your Username ",
            "team_name": "Give your team a name ",
            "email": "Email Id ",
            "college" : "Name of Your College",
            "phone_no" : "Contact # ",
        }
        help_texts = {
        "password" : "",
        }
class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username','team_name', 'email','college','phone_no')
