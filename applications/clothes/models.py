from django.db import models

from applications.brand.models import Brand


class Clothes(models.Model):
    type_of_clothes = models.CharField(max_length=255)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, related_name='clothes')
    description = models.TextField()
    price = models.DecimalField(max_digits=11, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.type_of_clothes


class ClothesImage(models.Model):
    clothes = models.ForeignKey(Clothes, on_delete=models.CASCADE, related_name='image')
    image = models.ImageField(upload_to='')

    def __str__(self):
        return self.clothes.type_of_clothes


