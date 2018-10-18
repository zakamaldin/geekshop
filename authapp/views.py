from django.shortcuts import render, HttpResponseRedirect
from authapp.forms import (
    ShopUserLoginForm,
    ShopUserRegisterForm,
    ShopUser
    )
from django.contrib import auth
from django.urls import reverse


def login(request):
    title = 'Enter'
    template = 'authapp/user.html'

    form = ShopUserLoginForm(data=request.POST)
    if request.method == 'POST' and form.is_valid():
        usr = request.POST['username']
        pwd = request.POST['password']
        user = auth.authenticate(username=usr, password=pwd)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('main'))
    content = {'title': title, 'form': form, 'type': 'log-user', 'text': 'Sign In', 'button': title}
    return render(request, template, content)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main'))


def edit(request):
    title = request.user.first_name
    template = 'authapp/user.html'
    user = ShopUser.objects.get(username=request.user)
    form = ShopUserRegisterForm(instance=user)
    if request.method == 'POST' and 'edit' in request.POST:
        form = ShopUserRegisterForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('auth:login'))
    if request.method == 'POST' and 'delete' in request.POST:
        user.delete()
        return HttpResponseRedirect(reverse('main'))
    content = {'title': title, 'form': form, 'type': 'edit', 'text': title, 'button': 'Edit'}
    return render(request, template, content)


def register(request):
    title = 'Registration'
    template = 'authapp/user.html'
    if request.method == 'POST':
        form = ShopUserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        form = ShopUserRegisterForm()
    content = {'title': title, 'form': form, 'type': 'register', 'text': 'Log In', 'button': 'Log In'}
    return render(request, template, content)




