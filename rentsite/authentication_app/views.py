from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib import messages
from userprofile.forms import UserCreateForm

def register(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get("email")
            user = authenticate(username=username, password=password, email=email)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreateForm()

    context = {'form': form}
    return render(request, 'authentication_app/register.html', context)


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('index')
    return render(request, 'authentication_app/login.html')


def password_edit(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Ваш пароль успешно изменен!')
            return redirect('password_edit')
        else:
            messages.error(request, 'Исправьте ошибки!')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'authentication_app/password_edit.html', {
        'form': form
    })
