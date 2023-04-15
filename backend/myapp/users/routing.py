from django.urls import re_path

from users import consumers


# import consumers

websocket_urlpatterns = [
    re_path(r'ws/my_consumer/$', consumers.ChatConsumer.as_asgi()),
]