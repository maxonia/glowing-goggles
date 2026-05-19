from django import forms
from django.contrib.auth.models import User
from .models import Task
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
    username = forms.CharField(label='Логин', max_length=150)
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)

class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput)
    email = forms.EmailField(required=True, label="Email")
    first_name = forms.CharField(required=True, label="Имя", max_length=30)
    last_name = forms.CharField(required=True, label="Фамилия", max_length=30)
    consent = forms.BooleanField(
        required=True,
        label='Я даю согласие на обработку персональных данных'
    )

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "password")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['text', 'comment', 'date', 'priority']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'text': forms.TextInput(attrs={'placeholder': 'Текст задачи'}),
            'comment': forms.Textarea(attrs={'placeholder': 'Комментарий (необязательно)'})
        }

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')
    first_name = forms.CharField(max_length=30, required=True, label='Имя')
    last_name = forms.CharField(max_length=30, required=True, label='Фамилия')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')