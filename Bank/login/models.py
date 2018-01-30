# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from unittest.util import _MAX_LENGTH

# Create your models here.
class Login(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    
class Post(models.Model):
    title=models.CharField(max_length=200)
    desc=models.CharField(max_length=200)
    
    def __str__(self):
        return self.title
    
class Category(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    
class Profile(models.Model):
    name=models.CharField(max_length=200)
    picture=models.ImageField(upload_to='pictures')

    class Meta:
        db_table="profile"