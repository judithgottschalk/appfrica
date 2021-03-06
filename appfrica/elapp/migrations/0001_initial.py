# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-22 13:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseName', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('editUsers', models.BooleanField(default=False)),
                ('editAdmins', models.BooleanField(default=False)),
                ('seeAllResults', models.BooleanField(default=False)),
                ('seeAllCouresSystemWide', models.BooleanField(default=False)),
                ('editExercisesSystemWide', models.BooleanField(default=False)),
                ('publishSystemWide', models.BooleanField(default=False)),
                ('enrolStudentsSystemWide', models.BooleanField(default=False)),
                ('assignStudents', models.BooleanField(default=False)),
                ('createSeminariesSystemwide', models.BooleanField(default=False)),
                ('seeCoursesSeminarywide', models.BooleanField(default=False)),
                ('editExcercisesSeminarywide', models.BooleanField(default=False)),
                ('createCoursesSeminarywide', models.BooleanField(default=False)),
                ('publishSeminarywide', models.BooleanField(default=False)),
                ('seeCoursesWhereTeacher', models.BooleanField(default=False)),
                ('seeResultsWhereTeacher', models.BooleanField(default=False)),
                ('editExcericesWhereTeacher', models.BooleanField(default=False)),
                ('enrollStudentsSeminaryWide', models.BooleanField(default=False)),
                ('unenrollStudentsSeminaryWide', models.BooleanField(default=False)),
                ('enrolStudentsWhereTeacher', models.BooleanField(default=False)),
                ('unenrolStudentsWhereTeacher', models.BooleanField(default=False)),
                ('assignTeachersSystemwide', models.BooleanField(default=False)),
                ('assignTeachersSeminarywide', models.BooleanField(default=False)),
                ('addBooksSystemwide', models.BooleanField(default=False)),
                ('addVideosSystemwide', models.BooleanField(default=False)),
                ('addAudiosSystemwide', models.BooleanField(default=False)),
                ('deleteBooksSystemwide', models.BooleanField(default=False)),
                ('deleteVideosSystemwide', models.BooleanField(default=False)),
                ('deleteAudiosSystemwide', models.BooleanField(default=False)),
                ('addBooksWhereTeacher', models.BooleanField(default=False)),
                ('addVideosWhereTeacher', models.BooleanField(default=False)),
                ('addAudiosWhereTeacher', models.BooleanField(default=False)),
                ('deleteBooksWhereTeacher', models.BooleanField(default=False)),
                ('deleteVideosWhereTeacher', models.BooleanField(default=False)),
                ('deteleAudiosWhereTeacher', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='RolePermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permissionID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elapp.Permission')),
                ('roleID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elapp.Role')),
            ],
        ),
        migrations.CreateModel(
            name='Seminary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seminaryName', models.CharField(max_length=255)),
                ('courseID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elapp.Course')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=255)),
                ('lastName', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('photoref', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='UserCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elapp.Course')),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elapp.User')),
            ],
        ),
        migrations.AddField(
            model_name='role',
            name='userID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elapp.User'),
        ),
    ]
