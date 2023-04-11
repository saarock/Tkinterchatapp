from tkinter import *
import tkinter as tk
# import speech_recognition as sr


# Install the window
root = Tk()

root.title("Singup")



# For voice recogination;
# for index, name in enumerate(sr.Microphone.list_microphone_names()):
#     print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))




# My singup first page
def page1():
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






# Sinin second page after singup user/client is able to visit this page
def page2():
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
    for_singin =Button(text="Singin", borderwidth=4, font=12)
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