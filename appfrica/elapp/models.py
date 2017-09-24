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

class Role(models.Model):
    role = models.CharField(max_length=255)
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
        
class Permission(models.Model):
    editUsers = models.BooleanField(default=False)
    editAdmins = models.BooleanField(default=False)
    seeAllResults = models.BooleanField(default=False)
    seeAllCouresSystemWide = models.BooleanField(default=False)
    editExercisesSystemWide = models.BooleanField(default=False)
    publishSystemWide = models.BooleanField(default=False)
    enrolStudentsSystemWide=models.BooleanField(default=False)
    assignStudents = models.BooleanField(default=False)
    createSeminariesSystemwide = models.BooleanField(default=False)
    seeCoursesSeminarywide = models.BooleanField(default=False)
    editExcercisesSeminarywide = models.BooleanField(default=False)
    createCoursesSeminarywide = models.BooleanField(default=False)
    publishSeminarywide = models.BooleanField(default=False)
    seeCoursesWhereTeacher = models.BooleanField(default=False)
    seeResultsWhereTeacher = models.BooleanField(default=False)
    editExcericesWhereTeacher = models.BooleanField(default=False)
    enrollStudentsSeminaryWide = models.BooleanField(default=False)
    unenrollStudentsSeminaryWide = models.BooleanField(default=False)
    enrolStudentsWhereTeacher = models.BooleanField(default=False)
    unenrolStudentsWhereTeacher = models.BooleanField(default=False)
    assignTeachersSystemwide = models.BooleanField(default=False)
    assignTeachersSeminarywide = models.BooleanField(default=False)
    addBooksSystemwide = models.BooleanField(default=False)
    addVideosSystemwide = models.BooleanField(default=False)
    addAudiosSystemwide = models.BooleanField(default=False)
    deleteBooksSystemwide = models.BooleanField(default=False)
    deleteVideosSystemwide = models.BooleanField(default=False)
    deleteAudiosSystemwide = models.BooleanField(default=False)
    addBooksWhereTeacher = models.BooleanField(default=False)
    addVideosWhereTeacher = models.BooleanField(default=False)
    addAudiosWhereTeacher = models.BooleanField(default=False)
    deleteBooksWhereTeacher = models.BooleanField(default=False)
    deleteVideosWhereTeacher = models.BooleanField(default=False)
    deteleAudiosWhereTeacher = models.BooleanField(default=False)
    
class RolePermission(models.Model):
    roleID = models.ForeignKey(Role, on_delete=models.CASCADE)
    permissionID = models.ForeignKey(Permission, on_delete=models.CASCADE)
    
    
    
    
    