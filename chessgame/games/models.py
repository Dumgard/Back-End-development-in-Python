from django.db import models

from players.models import Player


class Game(models.Model):
    player1 = models.OneToOneField(Player, null=True, on_delete=models.SET_NULL,
                                   verbose_name='Белые', related_name='player1')
    player2 = models.OneToOneField(Player, null=True, on_delete=models.SET_NULL,
                                   verbose_name='Чёрные', related_name='player2')
    notation = models.CharField(null=False, max_length=80,
                                verbose_name='Нотация Форсайда-Эдвартса (FEN)')
    status = models.IntegerField(null=False, default=2, verbose_name='Текущее состояние игры')
    time_last_move = models.DateTimeField(auto_now=True, verbose_name='Время последнего хода')
    time_start = models.DateTimeField(auto_now_add=True, verbose_name='Время начала партии')
    time_end = models.DateTimeField(null=True, verbose_name='Время окончания партии')
