import datetime
import pytz
import os

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, FileResponse
from django.views.generic import View, DetailView, ListView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile, Work, Issue, Text

from .serializers import IssueSerializer, WorkSerializer
from rest_framework import generics, permissions, renderers, viewsets

utc = pytz.UTC

# Create your views here
class HomeView(View):
    def get(self, *args, **kwargs):
        #get elements for landing page
        try:
            last_issue = Issue.objects.latest()
        except Issue.DoesNotExist:
            last_issue = None
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

"""
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
"""

class WorksView(ListView):
    model = Work
    paginate_by = 10
    template_name = "main/gridworks.html"


"""   
class WorkDetailView(DetailView):
    model = Work
    template_name = "main/work.html"
"""

class AddWorkView(View):
    def get(self, *args, **kwargs):
        return render(self.request, "main/addwork.html")

class PublishView(View):
    def get(self, *args, **kwargs):
        return render(self.request, "main/publica.html")

class ProfileView(LoginRequiredMixin, View):
    
    def get(self, request, *args, **kwargs):
        return render(self.request, "main/profile.html")

class SubscribeView(LoginRequiredMixin, View):
    
    def get(self, request, *args, **kwargs):
        p = Profile.objects.get(user=request.user)
    
        subscribed = p.membership_due_date >= utc.localize(datetime.datetime.now())
        context = {
            "subscribed": subscribed
        }
        return render(self.request, "main/subscribe.html", context)

class MembershipView(View):
    pass


#Api views
class IssueViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer

class WorkViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer

@login_required
def serve_protected_document(request, file_):
    p = Profile.objects.get(user=request.user)

    if p.membership_due_date >= utc.localize(datetime.datetime.now()):

        document = get_object_or_404(Text, pdf_file="protected/" + file_)
        path, file_name = os.path.split(file_)
        response = FileResponse(document.pdf_file,)
        return response

    else:
        return HttpResponse("redirect to suscription page")
