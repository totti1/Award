from django import forms
from .models import Project, Profile

class AddProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['pub_date', 'user', 'profile']

class AddProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']