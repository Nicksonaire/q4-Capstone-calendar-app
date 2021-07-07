from django import forms

class MyUserForm(forms.Form):
    email = forms.EmailField(max_length=40)
    name = forms.CharField(max_length=40)
    age = forms.IntegerField()
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)