from django import forms

class UserRegistrationForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form_control','placeholder':'Enter Your Username'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form_control','placeholder':'Enter Your Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form_control','placeholder':'Enter Your Password'}))
