from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null = True, blank = True)     # directly linking it to django's built in User model (if user is deleted, the profile model will also be deleted)
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    username = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    short_intro = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(max_length=200, null=True, blank=True, upload_to='profiles/', default="profiles/user-default.png")
    social_github = models.CharField(max_length=200, null = True, blank = True)     # directly linking it to django's built in User model (if user is deleted, the profile model will also be deleted)
    social_twitter = models.CharField(max_length=200, null = True, blank = True)     # directly linking it to django's built in User model (if user is deleted, the profile model will also be deleted)
    social_linkedin = models.CharField(max_length=200, null = True, blank = True)     # directly linking it to django's built in User model (if user is deleted, the profile model will also be deleted)
    social_youtube = models.CharField(max_length=200, null = True, blank = True)     # directly linking it to django's built in User model (if user is deleted, the profile model will also be deleted)
    social_website = models.CharField(max_length=200, null = True, blank = True)     # directly linking it to django's built in User model (if user is deleted, the profile model will also be deleted)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=True)
    def __str__(self):
        return str(self.user.username)

class Skilll(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)    # CASCADE: if owner is deleted, skill is also deleted
    name = models.CharField(max_length=200, blank=True, null=True)
    descrption = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=True)
    def __str__(self):
        return str(self.name)