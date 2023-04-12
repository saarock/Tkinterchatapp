from tkinter import *
import tkinter as tk
import requests as rq
import json
# import speech_recognition as sr


# Install the window
root = Tk()

root.title("Singup")



# For voice recogination;
# for index, name in enumerate(sr.Microphone.list_microphone_names()):
#     print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))




def home_page_for_chat():
    root.title("Chat")
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



    response = session.post(url, data=json.dumps(users_data), timeout=10, headers=headers)

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