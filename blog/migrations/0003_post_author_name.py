# Generated by Django 3.0.8 on 2020-07-22 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author_name',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
