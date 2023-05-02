from tkinter import *
import tkinter as tk
import requests as rq
import json
import websocket
import threading
import time
from tkinter import font
# websocket.enableTrace(True)
# websocket.WebSocketApp()


import json

# import speech_recognition as sr


# Install the window
root = Tk()

root.title("Singup")

global track_the_chatpage, track_the_homepage
track_the_homepage = True
track_the_chatpage = True
one_time_one_message = True
# For voice recogination;
# for index, name in enumerate(sr.Microphone.list_microphone_names()):
#     print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))
# global my_chat_frame

def on_message(ws, message):
   print("WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL")
   print(message)
   global one_time_one_message
#    if one_time_one_message: 
 
   message_real_time = json.loads(message)
   if message_real_time['id'] == for_name_email.get():
        my_chat_frame.insert('end', f"me => {message_real_time['message']}")
        my_chat_frame.itemconfigure(0, fg='white', bg='red')
        one_time_one_message = True
        return
        # print("Matched")
   else:
        my_chat_frame.insert('end', f" {message_real_time['id']} => {message_real_time['message']}")
        one_time_one_message = True
        # my_chat_frame.itemconfig(1, fg='white', bg='black')
        for i in range(my_chat_frame.size()):
          my_chat_frame.itemconfig(i, fg='white', bg='black')

#    else:
    #   print("Message ALREADY SEND")  
  

    

# Function to handle WebSocket errors
def on_error(ws, error):
    print("WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL1")

    print("WebSocket error: ", error)

# Function to handle WebSocket close events
def on_close(ws):
    print("WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL2")

    print("WebSocket closed")


# Create a WebSocket object

# For home
my_chat_frame = ''
def for_home():
   global track_the_homepage
   if track_the_homepage: 
    # my_chat_frame.destroy()

      my_chat_frame.place_forget()
      scrollbar.destroy()
      chat_box.destroy()
      send_button.destroy()
      send_entry.destroy()


    # custom_font.des
      print("I AM PRINTING....")
    
   
      print("Home Starting")
    #   if my_chat_frame:
    #        my_chat_frame.destroy()
    #        scrollbar.destroy()
    #        chat_box.destroy()
    #        send_button.destroy()
    #        send_entry.destroy()

    #   else:
    #        print('No any pack')       
        # my_chat_frame.pack_forget()
        # my_chat_frame.place_forget()
        # send_button.pack_forget()
        # send_entry.pack_forget()
        # send_button.destroy()
        # send_entry.destroy()
        # my_chat_frame.place_forget()
    

#  my_chat_frame, chat_box, scrollbar, custom_font





    # else:
        # print('No pack')    
    # my_chat_frame.pack_forget()
    # print(socketio.gethostname)
      user_unique_id = for_name_email.get()
      print(user_unique_id)






      global ws
      ws.close()
    # ws = websocket.WebSocket()
    #   ws = websocket.WebSocketApp('ws://localhost:8000/ws/my_consumer/test_room/',  on_message = on_message, on_error = on_error, on_close = on_close)
    # ws.connect("ws://localhost:8000/ws/my_consumer/test_room/")
    #   ws.on_open = lambda _: print("Connection is open")
    #   threading.Thread(target=ws.run_forever).start()
   


   
    #   print('Webscoket is Connected')
    #   send_message = {
    #     'id': user_unique_id,
    #     'message': "Hello aaysh banset"
    # }

    # pause for 2sec
    #   time.sleep(2)
    # s = json.dumps(send_message)
    # ws.send(s)


    
    # messgae = ws.recv()
    # print(messgae, "THIS IS THE MESSAGE OF THE GROPU MESSASGESSS WHICH IS BESTTER")


    # ws.on_message = on_message

    

    
  

    # try:
        
    #  print("Directly message")
    #  m = json.loads({'name': "basnet"})
    
     
    # except json.JSONDecodeError:
    #     print("Invalid Json data")    
    #     return

     # message = Label(text=m['message'])
     # message.pack()
    # print(m, "This ARE THE PURE MESSAGES")
    # print(type(m), "This is the type")
     # n = json.loads(m)
    # if 'message' in m:
        # print('yes there is messgae')
        # mes = Label(text=m['message'] )
        # mes.pack()
        # print(m['message'])

    # else: 
        # print("There is no messge")    
    #   global track_the_chatpage
      global my_name, track_the_chatpage
      welcome_message.config(text="Chat WITH YOUR FRIENDS CAREFULLY. PLEASED NOTE! CHAT IN POPER MANNER", font=1000,background='blue', fg='white' , borderwidth=12, border=12  )
      welcome_message.pack()
      my_name = Label(text='AAaysh', width=12)
      my_name.pack()
      track_the_homepage = False
      track_the_chatpage = True
   else:
    pass 

    
    #   global my_name
    #   welcome_message.config(text="Chat WITH YOUR FRIENDS CAREFULLY. PLEASED NOTE! CHAT IN POPER MANNER", font=1000,background='blue', fg='white' , borderwidth=12, border=12  )
    # welcome_message.pack()
    # my_name = Label(text='AAaysh', width=12)
    # my_name.pack()
    # print("Clciked")

     




def for_chat():
    global track_the_chatpage, track_the_homepage
    if track_the_chatpage:
     track_the_chatpage = False
     track_the_homepage = True

     
     
     print("I am running")
     # respons = session.get('http://localhost:8000/get_csrf_token/')
    # session = rq.Session()
    # csrftoken = respons.cookies['csrftoken']
    # headers = {'X-CSRFToken': csrftoken}
    # proxies = {'http': 'http://myproxy.com:8000', 'https': 'http://myproxy.com:8000'}

    # urls
    # url = 'http://localhost:8000/getmessage/'

        
        # for message in messages:
        #     print(message, "IDICCHCHHA  GAUTAM IDICHHHA GAUTAM IDICHCHHA GAUTAM")
     

        #     l = Label(my_chat_frame, text= 'meessgae')
        #     l.pack()
        # print(messages, "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")

    # if response.status_code == 200:
    #     home_page_for_chat()


    # def on_message(ws, message):
    # ws = websocket.WebSocket()
    # ws.connect("ws://localhost:8000/ws/my_consumer/test_room/")
     global ws
    # ws = websocket.WebSocket()
     ws = websocket.WebSocketApp('ws://localhost:8000/ws/my_consumer/test_room/',    on_message = on_message, on_error = on_error, on_close = on_close)
    # ws.connect("ws://localhost:8000/ws/my_consumer/test_room/")
     ws.on_open = lambda _: print("Connection is open")
     threading.Thread(target=ws.run_forever).start()
   


   
     print('Webscoket is Connected')
     send_message = {
         'id':  "12345",
         'message': "Hello aaysh banset"
     }
    # delay for two second
     time.sleep(2)

      









    # if my_name:
    #    my_name.pack_forget()
    # else:
    #  print("There is no any Pack")   
     
     def send_messages():
       global one_time_one_message
       if one_time_one_message:
      
        one_time_one_message = False
      
        my_message = send_entry.get()
        id = for_name_email.get()
        print("The message is this", my_message)
        print('Starting the send_messssssssgae OKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK')
        
        send_message = {
        'id': id,
        'message': my_message
    }
        s = json.dumps(send_message)

        if send_message['message']:
         ws.send(s)
        else:
         print('Simply the tracker is false')
        return  

    #   send_entry.event_add
    #   l = ws.recv()
    #   print(l, "THE MESSAGE THAT IS cOMWfROM THE SERVER")

    
    # my_chat = Label(text="Chat majaalya", width=12)

    # my_chat.pack()
     global my_chat_frame, chat_box, scrollbar, custom_font
     scrollbar = tk.Scrollbar(root)
     scrollbar.pack(side="right", fill="y")
     custom_font = tk.font.Font(size=40)
     my_chat_frame= Listbox(root, yscrollcommand=scrollbar.set, font=custom_font)
     my_chat_frame.place(x=300, y=150, height=550, width=950)


    #  scrollbar = tk.Scrollbar(my_chat_frame)
   

    # Create a Scrollbar widget and associate it with the Text widget

    #  scrollbar.pack(fill=Y)
    # chat_box.config(yscrollcommand=scrollbar.set)
     chat_box = tk.Text(my_chat_frame, yscrollcommand=scrollbar.set)

     global send_button, send_entry
     send_entry = Entry( font=233)
     send_button = Button( text="Send", font=233, command= send_messages)
     send_button.pack(side=BOTTOM)
     send_entry.pack(side=BOTTOM)
# requesting the server fot getting the messages
     response = rq.get('http://localhost:8000/getmessage/')
     data = response.json()


    

   




    #  get the data from the server
     labels = []
     if data['status'] == 'success':
        messages = data['message']
       
        for message in messages:
            if message['sender'] == for_name_email.get():
                my_label = tk.Label(my_chat_frame, text=message['message'])
                my_label.pack(side=tk.RIGHT)
            
                return

            else: 
                return  
    #  global  track_the_homepage     
     track_the_chatpage = False
     track_the_homepage = True
     print(track_the_chatpage)









def home_page_for_chat():

     label_title.pack_forget()
     label_name.pack_forget()
     label_email.pack_forget()
     label_password.pack_forget()
     label_repassword.pack_forget()
     for_name_input.pack_forget()
     for_name_email.pack_forget()
     for_name_password.pack_forget()
     for_name_repassword.pack_forget()
     for_singup_button.pack_forget()
     welcome_message.pack_forget()
     for_singin.pack_forget()
     for_singin_button.pack_forget()


# Starting the chat window or we can say new window after user sucessful the login level;
     try:
        # pass
    #   chat_window = tk.Tk()
    #   root.destroy()

     

       my_frame= Frame(bg="grey", borderwidth=6, relief=SUNKEN)
       my_frame.pack(side=LEFT, fill='y')
    #   l = Label( my_frame, text='Chat')
    #   l.pack(pady=142, padx=100)

       home_button = Button(my_frame,  text='Home', bg='black', fg='white', command=for_home, width=10)
       home_button.pack(padx=30)



       chat_button = Button(my_frame, text="Chat", fg="white", bg='black', command=for_chat, width=10)
       chat_button.pack(padx=30, pady=5)
       for_home()


     except Exception as e:
         print(e, "This is the error")  
   

 



# My singup first page
def page1():
    print('page1')

    label_title.pack_forget()
    label_name.pack_forget()
    label_email.pack_forget()
    label_password.pack_forget()
    label_repassword.pack_forget()
    for_name_input.pack_forget()
    for_name_email.pack_forget()
    for_name_password.pack_forget()
    for_name_repassword.pack_forget()
    for_singup_button.pack_forget()
    welcome_message.pack_forget()

    





def go_and_singin():
    headers = {'Content-Type': 'application/json'}
    name = for_name_input.get()

    email = for_name_email.get()
    password = for_name_password.get()



    users_data = {
        'name': name,
        'email': email,
        'password': password,
    
    }


    
    # print(name)
    session = rq.Session()
    # proxies = {'http': 'http://myproxy.com:8000', 'https': 'http://myproxy.com:8000'}

    # urls
    url = 'http://localhost:8000/signin/'



    response = session.post(url, data=json.dumps(users_data), timeout=4, headers=headers)

    if response.status_code == 200:
        home_page_for_chat()












# Sinin second page after singup user/client is able to visit this page
def page2():


    # Collect user Data
    name = for_name_input.get()
    email = for_name_email.get()
    password = for_name_password.get()
    repassword = for_name_repassword.get()



    # Packing the data into the  dictionary
    # Header 
    headers = {'Content-Type': 'application/json'}


    users_data = {
        'name': name,
        'email': email,
        'password': password,
        'repassword': repassword
    }


    
    # print(name)
    session = rq.Session()
    # proxies = {'http': 'http://myproxy.com:8000', 'https': 'http://myproxy.com:8000'}

    # urls
    url = 'http://localhost:8000/signup/'



    response = session.post(url, data=json.dumps(users_data), timeout=10, headers=headers)

    if response.status_code == 200:
        # print(response.text)
        print(response.json)
        print("Sucessfulll")
        root.title('Singin')
        label_title.pack_forget()
        label_name.pack_forget()
        label_email.pack_forget()
        label_password.pack_forget()
        label_repassword.pack_forget()
        for_name_input.pack_forget()
        for_name_email.pack_forget()
        for_name_password.pack_forget()
        for_name_repassword.pack_forget()
        for_singup_button.pack_forget()
        welcome_message.pack_forget()
    else: 
        print("Milyana")    
      


    # Un poack the UI from the window
    label_title.pack_forget()
    label_name.pack_forget()
    label_email.pack_forget()
    label_password.pack_forget()
    label_repassword.pack_forget()
    for_name_input.pack_forget()
    for_name_email.pack_forget()
    for_name_password.pack_forget()
    for_name_repassword.pack_forget()
    for_singup_button.pack_forget()
    welcome_message.pack_forget()

    

    # Again add the new Window
    welcome_message.config(text="Ok Singin pleased for chat", font=1000,background='blue', fg='white' , borderwidth=12, border=12  )
    welcome_message.pack()
    label_title.config(text="SINGIN")
    label_title.pack()
    label_name.pack(pady=6)
    for_name_input.pack(pady=6)
    label_email.pack(pady=6)
    for_name_email.pack(pady=6)
    label_password.pack(pady=6)
    for_name_password.pack(pady=6)
    global for_singin
    for_singin =Button(text="Singin", borderwidth=4, font=12, command=go_and_singin)
    for_singin.pack()
    for_singin_button.config(command=page1, text="Donot have Account => singin", bg="red", fg="white")
    for_singin_button.pack(pady=9)
  
   

    # label_title.pack()


   


# Welcome 32 Batche
welcome_message = Label(root, text="Welcome to you class Group chat Singup pleased for chat", font=1000,background='blue', fg='white' , borderwidth=12, border=12)




# lables
label_title = Label(root, text="SINGUP", font=102 , borderwidth=12, border=12)
label_name = Label(root, text="name", font=12)
label_email = Label(root, text='email', font=12)
label_password = Label(root, text='password', font=12)
label_repassword = Label(root, text='repassword', font=12)




# Set the border width and style
root.config(bd=19, relief='groove')

global for_name_email, for_name_password, for_name_repassword
# Inputs
for_name_input = Entry(root, width=21, font=12)
for_name_email = Entry(root, width=21, font=12)
for_name_password = Entry(root, width=21, font=12)
for_name_repassword = Entry(root, width=21, font=12)



# global for_singup_button
for_singup_button = Button(text="Singup", borderwidth=4, font=12, command=page2)
for_singin_button = Button(text="Already have Account => singin", borderwidth=4, font=12, command=page2, bg="red", fg="white")




# Pack the message
welcome_message.pack(pady=49)





# frame
tk_frame = Frame(root)
tk_frame.pack()





# pack to the screen
label_title.pack()
label_name.pack(pady=6)
for_name_input.pack(pady=6)

label_email.pack(pady=6)
for_name_email.pack(pady=6)


label_password.pack(pady=6)
for_name_password.pack(pady=6)



label_repassword.pack(pady=6)
for_name_repassword.pack(pady=6)


# button pack
for_singup_button.pack(pady=9)

# for_singin_button.pack(pady=5)



root.mainloop()