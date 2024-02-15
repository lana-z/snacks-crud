from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Snack(models.Model):
    name = models.CharField(max_length=256)
    purchaser = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    description = models.TextField(max_length=256)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    

