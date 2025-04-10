from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.urls import reverse_lazy

from app.models import Xabar
from .models import CustomUser

from .forms import CustomUserCreationForm, ProfileEditForm
from django.contrib.auth import login, logout, get_user_model


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"{user.username} muvaffaqiyatli ro'yxatdan o'tdi!")
            return redirect('app:home')
    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html', {'form': form})


@login_required
def profile(request):
    user = request.user
    return render(request, 'profile.html', {'user': user})


class CustomLoginview(LoginView):
    template_name = 'login.html'


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profil:profil')
    else:
        form = ProfileEditForm(instance=request.user)
    return render(request, 'edit_profile.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('app:home')


def s_prof(request, id):
    ss = get_object_or_404(CustomUser, id=id)

    return render(request, 's_detail.html', {'ss': ss})


def xabar_wr(request, id):
    if request.method == 'POST':
        desc = request.POST.get('desc')
        if desc:
            Xabar.objects.create(
                author=request.user,
                qabul=id,
                desc=desc
            )
            return redirect('profil:s_detail', id=id)

    return render(request, 'xabar_wr.html', {'q_id': id})
