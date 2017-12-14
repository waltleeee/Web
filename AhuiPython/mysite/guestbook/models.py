# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

"""
public class Post : models.Models {

    public string name {get; set;}
}

"""

class Post(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)