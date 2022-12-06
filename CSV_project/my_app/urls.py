from django.urls import path
from my_app import views


urlpatterns = [
    path('', views.StockMarketList.as_view(), name='stockmarket_list'),
    path('stock-form',views.StockMarketCreateView.as_view(), name='stock_form'),
    path('stock-form-update/<int:id>',views.StockMarketUpdateView.as_view(), name='stock_form_update'),
    path('stock-delete/<int:id>',views.StockMarketDeleteView.as_view(), name='stock_delete'),

]