from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


from .forms import SignUpForm


User = get_user_model()

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if not user:
            messages.error(request, "User not found")
            return render(request, 'account/login.html')
        login(request, user)
        messages.info(request, 'Login successfull!')
        return redirect('home')
    return render(request, 'account/login.html')


def logout_view(request):
    logout(request)
    messages.info(request, 'Logout successfull')
    return redirect('account:login')


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Siz ruyxatdan o`tdingiz')
            return redirect('account:login')
        messages.warning(request, 'qayta urinib kuring')

    form = SignUpForm()

    context = {
        'form': form,
    }

    return render(request, 'account/register.html', context)