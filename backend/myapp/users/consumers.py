import json

from channels.generic.websocket import WebsocketConsumer

print('Consumer')
class ChatConsumer(WebsocketConsumer):
    def connect(self):
        print('Connecting')
        self.accept()
        print('Socket Connected')

    def receive(self, text_data):
        # return super().receive(text_data)    
        print(text_data, 'This is messgae')  

    
    def chat_message(self, event):
        message = event['message']
        self.send(text_data=json.dumps(message))
     

    def disconnect(self, close_code):
        print('WebSocket Connection Closed')
        

    # def receive(self, text_data):
    #     text_data_json = json.loads(text_data)
    #     message = text_data_json["message"]

    #     self.send(text_data=json.dumps({"message": message}))

   