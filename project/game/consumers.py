import json
from channels.generic.websocket import WebsocketConsumer
from channels.generic.websocket import AsyncWebsocketConsumer
from django.shortcuts import render, get_object_or_404
from .game_objects.pgame import *
from .models import *
from channels.db import database_sync_to_async

active_games = {}

class gameConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_n = self.scope['url_route']['kwargs']['room_id']
        self.room_group_name = f'game_{self.room_n}'
        print(f"Room ID: {self.room_n}")

        
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        if self.room_n not in active_games :
            rooma = await self.get_room_data(self.room_n)
            active_games[self.room_n] = Game(rooma)
            await active_games[self.room_n].initialize_game(rooma)

            
            # await self.game_update({'data': active_games[self.room_n].get_data()})    
        
        await self.accept()


    @database_sync_to_async
    def get_room_data(self, room_id):
        return get_object_or_404(roomData, id=room_id)

    async def disconnect(self, close_code):
        print(f"Disconnecting from room: {self.room_n}")
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        await self.channel_layer.group_send(
            self.room_group_name,{
                'type': 'game_update',
                'data': active_games[self.room_n].name,
            }
        )

    async def game_update(self, event):
        data = event['data']
        await self.send(text_data=json.dumps(data))
        