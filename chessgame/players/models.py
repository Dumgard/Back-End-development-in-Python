from django.db import models


class Player(models.Model):
    nickname = models.CharField(max_length=32, null=False, blank=False, verbose_name='Никнейм')
    email = models.EmailField(null=False, blank=False, unique=True, verbose_name='Электронная почта')
    rating = models.IntegerField(null=False, blank=True, default=1200, verbose_name='Рейтинг')
    history = models.TextField(null=True, blank=True, verbose_name='История сыгранных партий')
