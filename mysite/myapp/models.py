from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.CharField(max_length=200)
    image = models.ImageField(blank=True, upload_to="images")
    seller = models.ForeignKey(User, default="1", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
