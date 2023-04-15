from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
from django.contrib.auth.models import User
# from django.contrib.admin import user
from django.contrib.auth import authenticate

from rest_framework_simplejwt.tokens import RefreshToken



# Create your views here.
@api_view(['POST'])
def sing_up(request):
    data = json.loads(request.body)
    print(data)
    name = data['name']
    email = data['email']
    password = data['password']
    repassword = data['repassword']
    print(name, email, password, repassword)
    if name and email and password and repassword is not None:
        try:
          # final_userdata = models.Users(name=name, email=email, password=password)
          user = User.objects.create_user(username=name, email=email, password=password)
          user.save()
          # final_userdata.save()
          print("Data is saved")
          return  Response({'message': 'Success!'})
        except Exception as e:
           print(e)  
        

    
    return  Response({'message': 'Success!'})




# For login page
@api_view(['POST'])
def sing_in(request):
   print("Request emit")
   data = json.loads(request.body)
   name = data['name']
   email = data['email']
   password = data['password']
   user = authenticate(request ,username =name ,email=email, password= password)
   if user is not None:
      print(user, "User is avialbel")

  #  referesh_token = RefreshToken.for_user(user)
  #  acess_token = str(referesh_token.access_token)

  #  print(acess_token, "This is acess Token")
  #  print(referesh_token, "This is referesh Token")
  # #  print(user)
  # #  return  Response({'acess_token': acess_token, 'referesh_token': referesh_token})
   return Response({'message': 'Done'})



   

# def get_allthe_users(request):
#    pass
