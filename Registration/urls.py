from django.urls import path
from .views import RegistrationCourse
urlpatterns = [
    path("registration/",RegistrationCourse,name="course"),
]
