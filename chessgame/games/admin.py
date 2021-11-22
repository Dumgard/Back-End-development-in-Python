from django.contrib import admin
from games.models import Game


class GameAdmin(admin.ModelAdmin):
    list_display = ('player1', 'player2', 'status', 'time_start', 'time_last_move', 'time_end')
    list_filter = ('status',)


admin.site.register(Game, GameAdmin)