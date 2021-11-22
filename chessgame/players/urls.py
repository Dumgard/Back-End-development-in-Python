from django.contrib import admin
from django.urls import path, include

from players.views import create, info, ratings, update, delete


urlpatterns = [
    path('new/', create, name='player_create'),
    path('info/<int:player_id>/', info, name='player_info'),
    path('rating/', ratings, name='player_ratings'),
    path('update/', update, name='player_update'),
    path('delete/', delete, name='player_delete'),
]