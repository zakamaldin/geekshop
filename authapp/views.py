from django.shortcuts import render, HttpResponseRedirect, redirect
from authapp.forms import (
    ShopUserLoginForm,
    ShopUserRegisterForm,
    )
from authapp.models import ShopUser
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.views.generic.edit import FormMixin
from django.conf import settings
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
    success_url = reverse_lazy('main')
    form = ShopUserRegisterForm()

    if request.method == 'POST':
        form = ShopUserRegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            auth.login(request, user)
            send_verify_mail(user)
        return redirect(success_url)

    return render(request, 'authapp/user.html', {'form': form,
                                                 'title': 'Registration',
                                                 'type': 'register',
                                                 'text': 'Log In',
                                                 'button': 'Log In'
                                                 }
                  )


def send_verify_mail(user):
    verify_link = reverse('auth:verify', args=[user.email, user.activation_key])

    title = f'Подтверждение учетной записи {user.username}'

    message = f'Для подтверждения учетной записи {user.username} на портале \
    перейдите по ссылке: \n{settings.DOMAIN_NAME}{verify_link}'

    return send_mail(title, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)


def verify(request, email, activation_key):
    success_url = reverse_lazy('main')
    try:
        user = ShopUser.objects.get(email=email)
        if user.activation_key == activation_key and not user.is_activation_key_expired():
            user.is_active = True
            user.save()
            auth.login(request, user)
            print(f'successfull activation user: {user}')
            return redirect(success_url)
        else:
            print(f'error activation user: {user}')
            return redirect(success_url)
    except Exception as e:
        print(f'error activation user : {e.args}')
        return redirect(success_url)
