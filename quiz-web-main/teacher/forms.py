from django import forms
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from . import models

class TeacherUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username', 'first_name','last_name','password']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': _('1234567')}),
            'first_name': forms.TextInput(attrs={'placeholder': _('Xodim ismi')}),
            'last_name': forms.TextInput(attrs={'placeholder': _('Xodim familiyasi')}),
            'password': forms.PasswordInput(attrs={'placeholder': _('Parol')})
        }

class TeacherForm(forms.ModelForm):
    class Meta:
        model=models.Teacher
        fields=['address','mobile']

