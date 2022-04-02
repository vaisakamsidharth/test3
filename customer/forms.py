from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from customer.models import Orders, Profile


class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]
        widget = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"})

        }


class LogInForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class OrderForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ["address"]
        widgets = {
            "address": forms.Textarea(attrs={"class": "form-control"})
        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ("user",)


class FeedBackForm(forms.Form):
    product_name = forms.CharField()
    feedback = forms.CharField()
