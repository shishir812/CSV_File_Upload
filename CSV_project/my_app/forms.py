from django import forms
from .models import StockMarket


class StockMarketForm(forms.ModelForm):
    class Meta:
        model = StockMarket
        fields = ['date', 'trade_code', 'high', 'low', 'open', 'close', 'volume']