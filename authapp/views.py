from django.shortcuts import render, HttpResponseRedirect
from authapp.forms import (
    ShopUserLoginForm,
    ShopUserRegisterForm,
    )
from authapp.models import ShopUser
from django.contrib import auth
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.views.generic.edit import FormMixin
from django.core.mail import send_mail


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


class RegisterView(CreateView):
    model = ShopUser
    template_name = 'authapp/user.html'
    form_class = ShopUserRegisterForm
    success_url = reverse_lazy('auth:login')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['title'] = 'Registration'
        context['type'] = 'register'
        context['text'] = 'Log In'
        context['button'] = 'Log In'
        return context



def account_signin(request):
    success_url = reverse_lazy('main:index')
    form = ShopUserRegisterForm()

    if request.method == 'POST':
        form = ShopUserRegisterForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            send_mail(
                'Signin User',
                f'Test Message.',
                from_email='info@project.ru',
                recipient_list=[email],
            )

    return render(request, 'authapp/user.html', {'form': form,
                                                 'title': 'Registration',
                                                 'type': 'register',
                                                 'text': 'Log In',
                                                 'button': 'Log In'
                                                 }
                  )



