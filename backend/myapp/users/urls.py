
from django.urls import path
from users import views

urlpatterns = [
  path('signup/', views.sing_up, name="Signup"),
  path('signin/', views.sing_in, name='SINGIN')
]