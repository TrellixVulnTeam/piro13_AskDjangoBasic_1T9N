from django.db import models
from django.conf import settings
from askcompany.utils import uuid_upload_to
from django.urls import reverse

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(blank=True) #길이제한 없음
    price = models.PositiveIntegerField()
    photo = models.ImageField(blank=True, upload_to = uuid_upload_to)
    is_publish = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta: # model class에 ordering 지정하기
        ordering = ['id']

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        #return reverse('shop:item_detail', args=[self.pk])
        return reverse('shop:item_detail', kwargs={'pk':self.pk})

# #blog model
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     title = models.CharField(max_length=100, db_index=True)
#     slug = models.SlugField(allow_unicode=True, db_index=True)
#     content = models.TextField(blank=True)
#     image = models.ImageField(blank=True)
#     comment_count = models.PositiveIntegerField(default=0)
#     is_publish = models.BooleanField(default=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
