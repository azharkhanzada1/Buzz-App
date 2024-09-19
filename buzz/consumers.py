import json
from channels.generic.websocket import AsyncWebsocketConsumer

class PostConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("posts_group", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("posts_group", self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        post_id = data["post_id"]

        # Send post data to group
        await self.channel_layer.group_send(
            "posts_group",
            {
                "type": "post_message",
                "message": post_id
            }
        )

    async def post_message(self, event):
        message = event['message']
        await self.send(text_data=json.dumps({
            'message': message
        }))