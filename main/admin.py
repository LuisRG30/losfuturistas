from django.contrib import admin
from .models import Profile, Message, Issue, Work

# Register your models here.

admin.site.register(Profile)
admin.site.register(Message)
admin.site.register(Issue)
admin.site.register(Work)