from django.urls import re_path
from .consumers import *

websocket_urlpatterns = [
    re_path (r'ws/offgame/(?P<room_id>\d+)/$', gameConsumer.as_asgi()),
    re_path (r'ws/onlinelobby/(?P<room_name>\w+)/$', OnLobbyConsumer.as_asgi()),

]
# (?P<room_name>\w+)