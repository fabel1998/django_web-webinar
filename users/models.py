from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
# модели = таблицы


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', blank=True)
    comment = models.ForeignKey('Comment', on_delete=models.PROTECT, null=True)


class Comment(models.Model):
    comment = models.TextField(verbose_name='Комментарий')

    def __str__(self):
        return self.comment
