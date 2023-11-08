from django.shortcuts import render, redirect
# Класс для створення форм
# from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm, ProfileImageForm, UserUpdateForm
# Класс для виводу сповіщення
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Створюємо перехід на сторінку реєстрації
def register(request):
    # Метод передачі даних (передає дані із форм)
    if request.method == 'POST':
        # В об'єкті form зберігаються дані отримані із форми
        form = UserRegisterForm(request.POST)
        # Валідація даних із форм
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            # Виводить сповіщення про успішну реєстрації
            messages.success(request, f'Користувач {username} був успішно створений!')
            # Після успішної реєстрації переходить на головну сторінку
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(
        request,
        'users/registration.html',
        {
            'title': 'Сторінка регістрації',
            'form': form
        }
    )

# Декоратор виконується до основної функції (перевірка чи авторизований користувач)
@login_required
def profile(request):
    if request.method == "POST":
        profileForm = ProfileImageForm(request.POST, request.FILES, instance=request.user.profile)
        updateUserForm = UserUpdateForm(request.POST, instance=request.user)

        if profileForm.is_valid() and updateUserForm.is_valid():
            updateUserForm.save()
            profileForm.save()
            messages.success(request, f'Ваш акаунт був успішно оновлений!')
            return redirect('profile')
    else:
        profileForm = ProfileImageForm(instance=request.user.profile)
        updateUserForm = UserUpdateForm(instance=request.user)
    
    data = {
        'profileForm': profileForm,
        'updateUserForm': updateUserForm,
    }

    return render(request, 'users/profile.html', data)