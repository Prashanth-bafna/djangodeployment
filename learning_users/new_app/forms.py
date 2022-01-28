from django import forms
from django.contrib.auth.models import User
from new_app.models import UserProfileInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields=('username', 'password','email')
class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model= UserProfileInfo
        fields=('portfilio_site','profile_pic')
