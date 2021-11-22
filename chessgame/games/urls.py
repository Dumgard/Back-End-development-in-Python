from django.contrib import admin
from django.urls import path, include

from games.views import new_board, list_board, info, render_board


urlpatterns = [
    path('new_board/', new_board, name='game_new_board'),
    path('list_board/', list_board, name='game_list_board'),
    path('info/<int:game_id>/', info, name='game_info'),
    path('render/', render_board, name='game_render_board'),
]
