from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf.urls import url



app_name = "main"
from .views import *



#Create a router for api viewsets
router = DefaultRouter()
router.register(r'issues', IssueViewSet)
router.register(r'works', WorkViewSet)


urlpatterns = [
    path("", HomeView.as_view(), name="index"),
    path("archive", ArchiveView.as_view(), name="archive"),
    path("issues", IssuesView.as_view(), name="issues"),
    #path("issue/<slug>", IssueDetailView.as_view(), name="issue"),
    path("works", WorksView.as_view(), name="works"),
    path("addworks", AddWorkView.as_view(), name="addwork"),
    #path("work/<slug>", WorkDetailView.as_view(), name="work"),
    path("publish", PublishView.as_view(), name="publish"),
    path("subscribe", SubscribeView.as_view(), name="subscribe"),
    path("profile", ProfileView.as_view(), name="profile"),
    url(r'^media/protected/(?P<file_>.*)$', serve_protected_document, name='serve_protected_document'),
    path("api/", include(router.urls))
]
