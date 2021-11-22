from django.contrib import admin
from players.models import Player


class PlayerAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'rating')
    list_filter = ('is_active',)


admin.site.register(Player, PlayerAdmin)
