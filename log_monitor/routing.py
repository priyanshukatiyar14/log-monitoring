# routing.py
from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/log/', consumers.LogConsumer.as_asgi()),
]
