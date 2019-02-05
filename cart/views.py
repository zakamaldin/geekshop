from django.shortcuts import render,redirect
from django.views.generic import (
    ListView, CreateView, DeleteView, UpdateView, DetailView
)
from django.urls import reverse_lazy
from django.forms import inlineformset_factory

from .models import Order, OrderItem
from .forms import OrderItemForm
from django.db.transaction import atomic
# Create your views here.


class OrderListView(ListView):
    model = Order
    template_name = 'cart/order_list.html'


class OrderCreateView(CreateView):
    model = Order
    fields = ['user', 'is_active']

    formset_model = OrderItem
    formset_fields = ['product', 'value']

    template_name = 'cart/order_detail.html'
    # login_url = reverse_lazy('auth:login')
    redirect_url = reverse_lazy('cart:order_list')
    success_url = reverse_lazy('cart:order_list')


    def get_formset_class(self):
        return inlineformset_factory(
            self.model,
            self.formset_model,
            fields=self.formset_fields,
        )

    def get_formset_kwargs(self):
        kwargs = {}

        if self.request.method in ('POST', 'PUT'):
            kwargs.update({
                'data': self.request.POST,
                'files': self.request.FILES,
            })

        if hasattr(self, 'object'):
            kwargs.update(
                **{'instance': self.object}
            )

        return kwargs

    def get_formset(self):
        formset_class = self.get_formset_class()
        prefix = formset_class.get_default_prefix()

        formset_kwargs = self.get_formset_kwargs()
        formset_kwargs.update(
            **{'prefix': prefix}
        )

        return formset_class(
            **formset_kwargs
        )

    def get_context_data(self, **kwargs):
        context = super(OrderCreateView, self).get_context_data(**kwargs)
        context.update({
            'formset': self.get_formset(),
            'button': 'Add',
            'type': 'create',
        })

        return context

    def form_valid(self, form):
        form = self.get_form()

        with atomic():
            self.object = form.save()
            formset = self.get_formset()

            if formset.is_valid():
                formset.save()

                return redirect(self.success_url)

        return render(self.request, self.template_name)


def cart_view(request):
    return render(request, 'cart/cart.html')


