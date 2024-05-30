from django.db import models
from django.db.models import CharField,ImageField,OneToOneField,CASCADE, DateTimeField,ForeignKey
from django.contrib.auth.models import User

import json
from datetime import date
from django.utils import timezone


class MustardSeed(models.Model):
    name = CharField(max_length=280, default="UNKNOWN")
    profile_picture = ImageField(upload_to="mustard_profile_pictures",null=True, blank=True)
    location = CharField(max_length=120, default="UNKNOWN")
    def get(self):
        total_members = len([p for p in Person.objects.filter(mustard_seed = self).all()])
        return {"id":self.id, "name":self.name, "profile_picture": self.profile_picture.url if self.profile_picture else "","members":total_members, "location":self.location}
    
    def update(self, data={}):

        try:
            for key in data.keys():
                setattr(self, key, data[key])
            self.save()
            return
        except Exception as e:
            return e

class Ministry(models.Model):
    name = CharField(max_length=280, default="UNKNOWN")
    profile_picture = ImageField(upload_to="ministry_profile_pictures",null=True, blank=True)

    def get(self):
        total_members = len([p for p in Person.objects.filter(ministry = self).all()])
        return {"id":self.id, "name":self.name, "profile_picture": self.profile_picture.url if self.profile_picture else "","members":total_members}
    
    def update(self, data={}):

        try:
            for key in data.keys():
                setattr(self, key, data[key])
            self.save()
            return
        except Exception as e:
            return e
    

class Position(models.Model):
    title = CharField(max_length=280, default="UNKNOWN")





class Person(models.Model):
    first_name = CharField(max_length=120, null=False,default="UNKNOWN")
    last_name = CharField(max_length=120,null=False, default="UNKNOWN")
    other_name = CharField(max_length=120, null=True, default="UNKNOWN")
    email = models.EmailField(unique=True,null=True)
    marital_status = CharField(max_length=28,null=True)
    gender = CharField(max_length=10, null=True)
    telephone = CharField(max_length=13, null=True, unique=True)
    location = CharField(max_length=120, null=True) 
    highest_education = CharField(max_length=120, null=True)
    profile_picture = ImageField(upload_to="profile_pictures",null=True, blank=True)

    dob = DateTimeField(default=timezone.now)
    first_appearance = DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    mustard_seed = models.OneToOneField(MustardSeed, on_delete=CASCADE, null=True)
    ministry = models.ForeignKey(Ministry, on_delete=CASCADE, null=True)#one person can belong to multiple ministries
    invitation_type = CharField(max_length=13, null=True)


    def __repr__(self) -> str:
        return f"<id: {self.id}, name: {self.first_name} />"

    def get(self):
        return {"id":self.id, "first_name":self.first_name, "last_name":self.last_name,"other_name":self.other_name,"email":self.email,"marital_status":self.marital_status,"gender":self.gender,"telephone":self.telephone,"location":self.location,"highest_education":self.highest_education,"profile_picture":"https://file.com" or self.profile_picture.url, "dob":str(self.dob), "first_appearance":str(self.first_appearance),"created_at":str(self.created_at),"updated_at":str(self.updated_at),"mustard_seed": self.mustard_seed.id,"ministry": self.ministry.id, "invitation_type":self.invitation_type}
            
    def update(self, data={}):
        try:
            for key in data.keys():

                if key == "ministry":
                    m = Ministry.objects.get(id = key)
                    self.ministry = m
                    self.save()
                if key == "mustard_seed":
                    m = MustardSeed.objects.get(id = key)
                    print(m.get())
                    self.mustard_seed = m
                    self.save()
                else:
                    setattr(self,str(key), data[key])
            self.save()
            return 
        except Exception as e:
            return e
        
        



class Member(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE, default=None)
    
class FirstTimer(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE, default=None)


class Visitor(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE, default=None)



def delete_and_create():
    Person.objects.all().delete()
    p = Person.objects.create(first_name="chris", last_name="lastname")