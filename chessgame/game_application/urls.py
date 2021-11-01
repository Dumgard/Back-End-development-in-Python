from django.contrib import admin
from django.urls import path, include

from game_application.views import new_board, list_board, info, render_board


urlpatterns = [
    path('new_board/', new_board, name='new_board'),
    path('list_board/', list_board, name='list_board'),
    path('info/<int:game_id>/', info, name='info'),
    path('render/', render_board, name='render_board'),
]
