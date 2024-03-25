from django import forms

class StudentLoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

class MentorLoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

class MentorApplicationForm(forms.Form):
    # Define fields for mentor application form
    # For example:
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    # Add more fields as needed
