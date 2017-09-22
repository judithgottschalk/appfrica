# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    photoref = models.CharField(max_length=255)
    
class Course(models.Model):
    courseName = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

class UserCourse(models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    courseID = models.ForeignKey(Course, on_delete=models.CASCADE)
       
class Seminary(models.Model):
    seminaryName = models.CharField(max_length=255)
    courseID = models.ForeignKey(Course, on_delete=models.CASCADE)
                                   
    