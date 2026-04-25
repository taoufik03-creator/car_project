from django.db import models

# Create your models here.

from django.urls import reverse
import uuid

class Car(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4)
    title=models.CharField(max_length=50,unique=True)
    make=models.CharField(max_length=100)
    model=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=20,decimal_places=2)

    def get_absolute_url(self):
        return reverse("car-details",kwargs={"pk":self.id})