from django.db import models
from django.db.models import CharField,ImageField,OneToOneField,CASCADE, DateTimeField,ForeignKey
from django.contrib.auth.models import User
import json
from datetime import date
from django.utils import timezone


class MustardSeed(models.Model):
    name = CharField(max_length=280, default="UNKNOWN")
    profile_picture = ImageField(upload_to="mustard_profile_pictures",null=True)
    location = CharField(max_length=120, default="UNKNOWN")

class Ministry(models.Model):
    name = CharField(max_length=280, default="UNKNOWN")
    profile_picture = ImageField(upload_to="ministry_profile_pictures",null=True)

class Position(models.Model):
    title = CharField(max_length=280, default="UNKNOWN")





class Person(models.Model):
    first_name = CharField(max_length=120, null=False,default="UNKNOWN")
    last_name = CharField(max_length=120,null=False, default="UNKNOWN")
    other_name = CharField(max_length=120, null=True, default="UNKNOWN")
    email = models.EmailField(unique=True,null=True)
    marital_status = CharField(max_length=28,null=True)
    gender = CharField(max_length=10, null=True)
    telephone = CharField(max_length=13, null=True)
    location = CharField(max_length=120, null=True) 
    highest_education = CharField(max_length=120, null=True)
    profile_picture = ImageField(upload_to="profile_pictures",null=True)

    dob = DateTimeField(default=timezone.now)
    first_appearance = DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    mustard_seed = models.OneToOneField(MustardSeed, on_delete=CASCADE, null=True)
    ministry = models.ForeignKey(Ministry, on_delete=CASCADE, null=True)#one person can belong to multiple ministries
    invitation_type = CharField(max_length=13, null=True)


class Member(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE, default=None)
    
class FirstTimer(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE, default=None)


class Visitor(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE, default=None)