from django.urls import path, include

app_name = "main"
from .views import *
urlpatterns = [
    path("", HomeView.as_view(), name="index")
]
