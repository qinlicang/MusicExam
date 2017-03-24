# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Answers(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    question_id = models.IntegerField()
    title = models.TextField(blank=True, null=True)  # This field type is a guess.
    img = models.TextField(blank=True, null=True)  # This field type is a guess.
    is_deleted = models.IntegerField()
    options = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'answers'


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Paper(models.Model):
    paper_id = models.IntegerField(primary_key=True)
    name = models.TextField()
    count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'paper'


class Question(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    paper_id = models.IntegerField()
    question_id = models.IntegerField()
    is_deleted = models.IntegerField()
    num = models.IntegerField()
    score = models.IntegerField()
    title = models.TextField(blank=True, null=True)  # This field type is a guess.
    titlesound = models.TextField(blank=True, null=True)  # This field type is a guess.
    image = models.TextField(blank=True, null=True)  # This field type is a guess.
    sound = models.TextField(blank=True, null=True)  # This field type is a guess.
    option_desc = models.TextField(blank=True, null=True)  # This field type is a guess.
    option_img = models.TextField(blank=True, null=True)  # This field type is a guess.
    correct = models.TextField(blank=True, null=True)  # This field type is a guess.
    label = models.TextField(blank=True, null=True)  # This field type is a guess.
    settings_field = models.TextField(db_column='settings\u3000\u3000\u3000', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'question'


class Respondents(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    pager_id = models.IntegerField()
    question_id = models.IntegerField()
    user_id = models.IntegerField()
    is_deleted = models.IntegerField()
    answer = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'respondents'
