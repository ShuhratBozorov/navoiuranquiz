from django import forms
from django.contrib.auth.models import User
from . import models
from quiz import models as QMODEL

class StudentUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
            'password': forms.PasswordInput()

            #   'username': forms.TextInput(attrs={'placeholder': '12345'}),
            # 'first_name': forms.TextInput(attrs={'placeholder': 'Ходим исми'}),
            # 'last_name': forms.TextInput(attrs={'placeholder': 'Ходим фамилияси'}),
            # 'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            # 'password': forms.PasswordInput(attrs={'placeholder': 'Parol'})
        }

class StudentForm(forms.ModelForm):
    class Meta:
        model=models.Student
        fields=['address','mobile','selected_subject','regions']

