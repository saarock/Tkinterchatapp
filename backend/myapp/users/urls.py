
from django.urls import path
from users import views
# from socketio import views as sio_views

urlpatterns = [
  path('signup/', views.sing_up, name="Signup"),
  path('signin/', views.sing_in, name='SINGIN'),
  path('getmessage/', views.get_message, name='get_message'),
  # path('socket.io/', sio_views.serve, name='socketio'),
]