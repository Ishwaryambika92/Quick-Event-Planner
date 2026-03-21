from django import forms
from .models import Event
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'date', 'time', 'location', 'image','fee']

        fields = '__all__' 
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

