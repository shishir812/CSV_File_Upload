from django.db import models

# Create your models here.
class StockMarket(models.Model):
    date = models.DateField(null=True)
    trade_code = models.CharField(null=True, max_length=100)
    high = models.CharField(null=True, max_length=100)
    low = models.CharField(null=True, max_length=100)
    open = models.CharField(null=True, max_length=100)
    close = models.CharField(null=True, max_length=100)
    volume = models.CharField(null=True, max_length=100)

    def __str__(self):
        return self.trade_code
