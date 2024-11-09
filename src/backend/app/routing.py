# routing.py - Django Channels routing setup for WebSocket communication

from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from . import consumers

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter([
            path('ws/real-time-updates/', consumers.LocationConsumer.as_asgi()),
        ])
    ),
})
