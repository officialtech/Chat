# sudo docker run -p 6379:6379 -d redis:5

from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('<str:room_name>/<str:username>/', views.chatRoom, name="chat"),
]
