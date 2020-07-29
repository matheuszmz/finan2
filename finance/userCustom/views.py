from django.contrib.auth import logout
from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserCreationForm
from .models import User


def my_logout(request):
    logout(request)
    return redirect('index')


def signup(request):
    form = UserCreationForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'signup.html', {'form': form, 'btn': 'Cadastrar'})


def user_data_change(request, id):
    user = get_object_or_404(User, pk=id)
    form = UserCreationForm(request.POST or None, request.FILES or None, instance=user)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'signup.html', {'form': form, 'btn': 'Alterar'})


