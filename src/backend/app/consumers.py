# consumers.py - WebSocket consumer to handle real-time location updates

from channels.generic.websocket import AsyncWebsocketConsumer
import json

class LocationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def receive(self, text_data):
        data = json.loads(text_data)
        # Handle location data here
        await self.send(text_data=json.dumps({"status": "received"}))
