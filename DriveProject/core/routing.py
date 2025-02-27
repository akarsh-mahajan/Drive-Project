from django.urls import path
from core.consumers import ChatConsumer
from channels.routing import ProtocolTypeRouter, URLRouter

websocket_urlpatterns = [
    path("ws/chat/", ChatConsumer.as_asgi()),
]

application = ProtocolTypeRouter({
    "websocket": URLRouter(websocket_urlpatterns),
})
