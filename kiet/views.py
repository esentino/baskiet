from django.shortcuts import render, redirect
from kiet.models import Baskiet, ProductInBaskietForm, Product
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.urls import reverse
# Create your views here.
class CreateBaskiet(CreateView):
    model = Baskiet
    fields = '__all__'
    success_url = '/create/'

class CreateProduct(CreateView):
    model = Product
    fields = '__all__'
    success_url = '/create/product'


class BaskietView(DetailView):
    model = Baskiet

    def get_context_data(self, **kwargs):
        context = super(BaskietView, self).get_context_data(**kwargs)
        calculation = self.object
        context['form'] = ProductInBaskietForm(initial={'baskiet': calculation})
        return context

    def post(self, request, pk):
        form = ProductInBaskietForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('baskiet', args=[pk]))
