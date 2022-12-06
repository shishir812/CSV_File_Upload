from django.core.management.base import BaseCommand
import pandas as pd
from my_app.models import StockMarket

class Command(BaseCommand):
    help = 'import booms'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        df = pd.read_csv('stock_market_data.csv')
        for DATE, TRADE_CODE, HIGH, LOW, OPEN, CLOSE, VOLUME in zip(df.date, df.trade_code, df.high, df.low, df.open, df.close, df.volume):
            models = StockMarket(date=DATE, trade_code=TRADE_CODE, high=HIGH, low=LOW, open=OPEN, close=CLOSE, volume=VOLUME)
            models.save()


