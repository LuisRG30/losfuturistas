from django.db.models.signals import post_save
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    membership_due_date = models.DateTimeField(blank=True, null=True)
    stripe_customer_id = models.CharField(max_length=255, blank=True, null=True)
    stripe_subscription_id = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}"


class Message(models.Model):
    name = models.CharField(max_length=32)
    email = models.EmailField()
    message = models.TextField(max_length=500)

    def __str__(self):
        return f"{self.name}  {self.email}"

class Label(models.Model):
    name = models.CharField(max_length=32)
    active = models.BooleanField()
    staff_only = models.BooleanField()

    def __str__(self):
        return f"{self.name}"

class Text(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100, blank=True, null=True)
    author = models.CharField(max_length=50)
    publication_date = models.DateField()
    sinopsis = models.TextField(max_length=1000)
    image = models.FileField(null=True, blank=True, upload_to="public")
    pdf_file = models.FileField(null=True, blank=True, upload_to="protected")
    slug = models.SlugField()
    label = models.ManyToManyField(Label, blank=True, null=True)

    class Meta:
        get_latest_by = 'publication_date'



class Issue(Text):
    
    def __str__(self):
        return f"{self.author}, {self.title}, {self.publication_date}"

    def get_absolute_url(self):
        return reverse("main:issue", kwargs={
            'slug': self.slug
        })


class Work(Text):
    display = models.BooleanField()

    def __str__(self):
        return f"{self.author}, {self.title}, {self.publication_date}"

    def get_absolute_url(self):
        return reverse("main:work", kwargs={
            'slug': self.slug
        })







def userprofile_receiver(sender, instance, created, *args, **kwargs):
    if created:
        userprofile = Profile.objects.create(user=instance)


post_save.connect(userprofile_receiver, sender=settings.AUTH_USER_MODEL)