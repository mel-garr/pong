# from django.urls import re_path

# from . import consumers

# websocket_urlpatterns = [
#     re_path(r"ws/chat/(?P<room_id>\w+)/$", consumers.ChatConsumer.as_asgi()),
# ]


from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r"ws/test2/(?P<room_id>\w+)/$", consumers.ChatConsumer.as_asgi()),  # Updated to 'room_id'
]
