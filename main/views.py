import datetime
import pytz

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View, DetailView, ListView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile, Work, Issue

from .serializers import IssueSerializer, WorkSerializer
from rest_framework import generics, permissions, renderers, viewsets

utc = pytz.UTC

# Create your views here
class HomeView(View):
    def get(self, *args, **kwargs):
        #get elements for landing page
        last_issue = Issue.objects.latest()
        displayables = Work.objects.filter(display=True)
        context = {
            "last_issue": last_issue,
            "displayables": displayables
        }
        return render(self.request, "main/index.html", context)

class ArchiveView(View):
    def get(self, *args, **kwargs):
        return render(self.request, "main/archive.html")

class IssuesView(ListView):
    model = Issue
    paginate_by = 10
    template_name = "main/grid.html"

class IssueDetailView(LoginRequiredMixin, DetailView):
    model = Issue
    template_name = "main/issue.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            p = Profile.objects.get(user=request.user)
            if p.membership_due_date >= utc.localize(datetime.datetime.now()):
                return self.get(request, *args, **kwargs)
            else:
                return HttpResponse("Suscríbete putito")
        else:
            return redirect("main:profile")
            

class WorksView(ListView):
    model = Work
    paginate_by = 10
    template_name = "main/grid.html"
    
class WorkDetailView(DetailView):
    model = Work
    template_name = "main/work.html"

class PublishView(View):
    def get(self, *args, **kwargs):
        return render(self.request, "main/publica.html")

class ProfileView(LoginRequiredMixin, View):
    
    def get(self, request, *args, **kwargs):
        return render(self.request, "main/profile.html")


#Api views
class IssueViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer

class WorkViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer