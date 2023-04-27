import json
from channels.layers import get_channel_layer
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from users import models


print('Consumer')

class ChatConsumer(WebsocketConsumer):
    channel_layer = get_channel_layer()
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']

        self.room_group_name = '%s' % self.room_name
    
        # print(self.channel_layer, "This is my Channel lllllllllllllLLLLLLLLLLLLLLLL")
      # Join the room group
        async_to_sync(self.channel_layer.group_add) (
            self.room_group_name,
            self.channel_name
            
        )

        
       


        # print(self.room_name, "And this is the Group name", self.room_group_name, "This is the ROOOM NAME")

        print('Connecting')
        self.accept()
        print(self.channel_name, 'HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH', "And this is the Group name", self.room_group_name,)
        print('Socket Connected')
    

    def receive(self, text_data):
        print("I am running...")
        let = json.loads(text_data)
        # return super().receive(text_data)    
        print(let['id'], let['message'], 'This is messgae')  

        a = {
            'id': let['id'],
            'message': "How are you"
        }

        
        # for now this will send the message to the same client who send the message it not broad caste the message
        # self.send(text_data=json.dumps({"message": text_data}))



        print('this is text data', type(let), text_data   )
        # broadcaste the message to all the Client
        #What can this method can do show all teh Things
        async_to_sync(self.channel_layer.group_send) (
        self.room_group_name,
        {
            #chat_message called if the message is send
            'type': 'chat_message',
            'message': let
        }
    )
        print(let, "This is letttttttttttttt")
        
        print(self.room_group_name, "THSISISISIISISISI")
        




    
    def chat_message(self, event):
        
      
                             

        message = event['message']
        print("I am calling", message)
        # sendinG the message to the socket
        mes = models.Messages(sender = message['id'], message = message['message'])
        mes.save()
        
        self.send(text_data=json.dumps(message))
        allthe_message = models.Messages.objects.all()
        for message in allthe_message:
            print(message.sender, "this are athe all the messages")
            print(message.message, "this are athe all the messages")
     

# Runs when socket Disconnected
    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

        
        print('WebSocket Connection Closed')
        

    # def receive(self, text_data):
    #     text_data_json = json.loads(text_data)
    #     message = text_data_json["message"]

    #     self.send(text_data=json.dumps({"message": message}))

   