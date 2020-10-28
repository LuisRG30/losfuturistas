from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Work, Profile, Issue

class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = ['title', 'subtitle', 'author', 'publication_date', 'sinopsis', 'pdf_file', 'display']

class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ['title', 'subtitle', 'author', 'publication_date', 'sinopsis', 'pdf_file']