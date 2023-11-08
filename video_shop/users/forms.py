# Описує поля в формі
from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm


# Форма для реєстрації на сайті
class UserRegisterForm(UserCreationForm):
    # required=True = Обов'язкове поле для заповнювання
    email = forms.EmailField(
        label='Введіть Email', 
        required=True,
        # (attrs={'class': 'form-control'}) Добавляє класс від Bootstrap
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваш Email'})
    )
    username = forms.CharField(
        label='Введіть логін',
        required=True, 
        help_text="Символи ( @, /, _ ) заборонені!",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваш логін'})
    )
    password1 = forms.CharField(
        label='Введіть пароль',
        required=True, 
        help_text="Пароль повинен містити 8 або більше символів!",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Ваш пароль'})
    )
    password2 = forms.CharField(
        label='Підтвердіть пароль',
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Повторіть пароль'})
    )

    # Порядок виведення форм
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# Форма для оновлення даних в кабінеті користувача
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(
        label='Введіть Email', 
        required=True,
        # (attrs={'class': 'form-control'}) Добавляє класс від Bootstrap
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваш Email'})
    )
    username = forms.CharField(
        label='Введіть логін',
        required=True, 
        help_text="Символи ( @, /, _ ) заборонені!",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваш логін'})
    )

    # Порядок виведення форм
    class Meta:
        model = User
        fields = ['username', 'email']

# Форма для завантаження фото в особистий профіль
class ProfileImageForm(forms.ModelForm):
    img = forms.ImageField(
        label='Завантажити фото', 
        required=False,
        widget=forms.FileInput
    )
        
    class Meta:
        model = Profile
        fields = ['img']