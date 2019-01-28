from django.db import models
from django.forms import ModelForm
# Create your models here.

class Baskiet(models.Model):
    name = models.CharField(max_length=255)

class Product(models.Model):
    name = models.CharField(max_length=255)


class ProductInBaskiet(models.Model):
    baskiet = models.ForeignKey(Baskiet, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.IntegerField()

    def __str__(self):
        return "{} {} {}".format(self.baskiet.name, self.product.name, self.count)

class ProductInBaskietForm(ModelForm):
    class Meta:
        model = ProductInBaskiet
        fields = '__all__'
