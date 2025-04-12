from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.contrib.auth.models import User
import random


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    captcha_answer = forms.IntegerField(label='', required=True)
    captcha_hidden = forms.IntegerField(widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

        self.num1 = random.randint(1, 10)
        self.num2 = random.randint(1, 10)

        self.fields['captcha_answer'].label = f"{self.num1} + {self.num2} = "
        self.fields['captcha_hidden'].initial = self.num1 + self.num2

    def clean(self):
        cleaned_data = super().clean()
        answer = cleaned_data.get("captcha_answer")
        correct = cleaned_data.get("captcha_hidden")

        if answer != correct:
            self.add_error('captcha_answer', "Noto'g'ri javob.")


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'phone_number', 'address', 'image', 't_me']


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'address', 'image', 't_me']
