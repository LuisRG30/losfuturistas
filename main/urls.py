from django.urls import path, include

app_name = "main"
from . import views
urlpatterns = [
    path("", views.index, name="index")
]
