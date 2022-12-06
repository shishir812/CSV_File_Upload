from django.shortcuts import render,get_object_or_404,reverse,redirect
from django.views import generic
from .models import StockMarket
from .forms import StockMarketForm
from django.contrib import messages



# Create your views here.

class StockMarketList(generic.ListView):
    template_name ='my_app/StockMarket_list.html'
    queryset = StockMarket.objects.all()
    paginate_by = 12
    ordering = ['id']


class StockMarketCreateView(generic.CreateView):
    template_name = 'my_app/StockMarket_create.html'
    form_class = StockMarketForm


    def get_success_url(self):
        messages.success(self.request, ('New Stock Added!!'))
        return reverse('stockmarket_list')


class StockMarketUpdateView(generic.UpdateView):
    template_name = 'my_app/StockMarket_create.html'
    form_class = StockMarketForm
    # queryset = Teacher.objects.all()


    def get_object(self):
        id = self.kwargs.get('id')
        return get_object_or_404(StockMarket, id=id)


    def get_success_url(self):
        messages.success(self.request, ('Stock information Updated!!'))
        return reverse('stockmarket_list')


class StockMarketDeleteView(generic.DeleteView):
    template_name = 'my_app/StockMarket_delete.html'

    def get_object(self):
        id = self.kwargs.get('id')
        return get_object_or_404(StockMarket, id=id)

    def get_success_url(self):
        messages.success(self.request, ('Stock id Deleted!!'))
        return reverse('stockmarket_list')


