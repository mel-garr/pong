import json
from channels.generic.websocket import WebsocketConsumer

class gameConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def dsiconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        self.send(text_data=json.dumps({'message':message}))

        