from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(blank=True) #길이제한 없음
    price = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


