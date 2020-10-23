from django.db.models.signals import post_save
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    membership_due_date = models.DateTimeField(blank=True, null=True)
    stripe_customer_id = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}"


class Message(models.Model):
    name = models.CharField(max_length=32)
    email = models.EmailField()
    message = models.TextField(max_length=500)

    def __str__(self):
        return f"{self.name}  {self.email}"


class Text(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100, blank=True, null=True)
    author = models.CharField(max_length=50)
    publication_date = models.DateField()
    sinopsis = models.TextField(max_length=1000)

class Issue(Text):
    pass

class Work(Text):
    display = models.BooleanField()





def userprofile_receiver(sender, instance, created, *args, **kwargs):
    if created:
        userprofile = Profile.objects.create(user=instance)


post_save.connect(userprofile_receiver, sender=settings.AUTH_USER_MODEL)