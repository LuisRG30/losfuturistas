from django.urls import path, include
from rest_framework.routers import DefaultRouter

app_name = "main"
from .views import *


#Create a router for api viewsets
router = DefaultRouter()
router.register(r'works', WorkViewSet)


urlpatterns = [
    path("", HomeView.as_view(), name="index"),
    path("archive", ArchiveView.as_view(), name="archive"),
    path("issues", IssuesView.as_view(), name="issues"),
    path("issue/<slug>", IssueDetailView.as_view(), name="issue"),
    path("works", WorksView.as_view(), name="works"),
    path("work/<slug>", WorkDetailView.as_view(), name="work"),
    path("publish", PublishView.as_view(), name="publish"),
    path("profile", ProfileView.as_view(), name="profile"),
    path("api/", include(router.urls))
]
