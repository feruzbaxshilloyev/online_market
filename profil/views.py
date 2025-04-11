from datetime import timezone

from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.urls import reverse_lazy

from app.models import Xabar
from .models import CustomUser, Chat

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


User = get_user_model()


@login_required
def chat_view(request, id):
    qabul = get_object_or_404(User, id=id)
    user = request.user
    if request.method == 'POST':
        desc = request.POST.get('desc')
        if 'mark_as_read' in request.POST:
            Chat.objects.update(is_view=True)
            return redirect('profil:chat', id=id)

        if desc:
            Chat.objects.create(
                author=request.user,
                receiver=qabul,
                desc=desc
            )
            return redirect('profil:chat', id=id)

    messages = Chat.objects.all().order_by('created_at')
    ctx = {'messages': messages, 'receiver': qabul, 'user': user, 'r_id': id}

    return render(request, 'xabar_wr.html', ctx)


@login_required
def edit_message(request, id):
    message = get_object_or_404(Chat, id=id, author=request.user)

    if request.method == 'POST':
        desc = request.POST.get('desc')
        if desc:
            message.desc = desc
            message.save()
            return redirect('profil:chat', id=1)

    return render(request, 'edit_message.html', {'message': message})


@login_required
def delete_message(request, id):
    message = get_object_or_404(Chat, id=id, author=request.user)

    if request.method == 'POST':
        message.delete()
        return redirect('profil:chat', id=1)

    return render(request, 'confirm_del.html', {'message': message})


def confirm_delete(request, id):
    message = get_object_or_404(Xabar, id=id)

    if request.method == "POST":
        message.delete()
        return redirect('profil:chat', r_id=message.receiver.id)

    return render(request, 'confirm_del.html', {'message': message, 'r_id': message.receiver.id})


def chat_list(request):
    ch = Chat.objects.all()
    chats = []

    return render(request, 'chatlar.html', {'chats': chats})
