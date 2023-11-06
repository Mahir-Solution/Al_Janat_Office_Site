from django.urls import path
from .views import home

urlpatterns = [
    path("",home,name="home"),
    #path("message/",Message,name="message"),
]

