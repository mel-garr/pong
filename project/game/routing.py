from django.urls import re_path
from .consumers import *

websocket_urlpatterns = [
    re_path (r'ws/offgame/(?P<room_id>\d+)/$', gameConsumer.as_asgi()),
]