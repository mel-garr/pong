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
            
        await self.accept()
        serialized_data = active_games[self.room_n].serialize_game_data()
        await self.channel_layer.group_send(
            self.room_group_name, {
                'type': 'game_update',
                'data': serialized_data,
            }
        )


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
        update = json.loads(text_data)
        # print (update)
        await active_games[self.room_n].updategame(update)
    #     await self.handle_player_action(player_name, action_type, action)
        serialized_data = active_games[self.room_n].serialize_game_data()
        await self.channel_layer.group_send(
            self.room_group_name,{
                'type': 'game_update',
                'data': serialized_data,
            }
        )

    async def handle_player_action(self, player_name, action_type, action):
        player = next((player for player in active_games[self.room_n].redteamplayers + active_games[self.room_n].blueteamplayers if player.name == player_name), None)

    async def game_update(self, event):
        data = event['data']
        await self.send(text_data=json.dumps(data))
        