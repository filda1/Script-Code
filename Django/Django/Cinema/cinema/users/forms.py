from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class RegistroForm(UserCreationForm):
    class Meta:
        model = User

        fields =  [
            'username',
            'first_name',
            'last_name',
            'email',
        ]

        labels = {
            'username':'Username',
            'first_name':'First Name',
            'last_name':'Last Name',
            'email':'Email',
        }

        widgets = {
            'username':forms.TextInput(attrs={'class':'w3-input w3-border','type':'text','placeholder':'Username','name':'nombre',}),
            'first_name':forms.TextInput(attrs={'class':'w3-input w3-border','type':'text','placeholder':'First Name','name':'nombre',}),
            'last_name':forms.TextInput(attrs={'class':'w3-input w3-border','type':'text','placeholder':'Last Name','name':'nombre',}),
            'email':forms.TextInput(attrs={'class':'w3-input w3-border','type':'text','placeholder':'Email','name':'nombre',}),
        }
