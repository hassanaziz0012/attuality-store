from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=500, unique=True)

    price = models.FloatField(default=0)
    discounted_price = models.FloatField(default=0)
    sizes = models.JSONField(null=True, blank=True)
    image = models.ImageField(upload_to="products/images")

    order = models.IntegerField(default=0, unique=True)

    def __str__(self) -> str:
        return f"{self.name}"

    def __repr__(self) -> str:
        return f'<Product: {self.name}>'
        