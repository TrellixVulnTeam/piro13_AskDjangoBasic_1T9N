from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(blank=True) #길이제한 없음
    price = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# #blog model
# class Post(models.Model):
#     author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     title = models.CharField(max_length=100, db_index=True)
#     slug = models.SlugField(allow_unicode=True, db_index=True)
#     content = models.TextField(blank=True)
#     image = models.ImageField(blank=True)
#     comment_count = models.PositiveIntegerField(default=0)
#     is_publish = models.BooleanField(default=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
