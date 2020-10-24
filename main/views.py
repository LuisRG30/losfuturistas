from django.shortcuts import render
from django.views.generic import View, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile

# Create your views here.ssdx
class HomeView(View):
    def get(self, *args, **kwargs):
        return render(self.request, "main/index.html")

class PublishView(View):
    def get(self, *args, **kwargs):
        return render(self.request, "main/publica.html")

class ProfileView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return render(self.request, "main/profile.html")