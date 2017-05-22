# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models

from login.models import Department


class Activity(models.Model):
    act_id = models.AutoField(primary_key=True)
    act_name = models.CharField(max_length=100)
    act_content = models.TextField()
    true_content = models.TextField()

    class Meta:
        managed = False
        db_table = 'activity'


class News(models.Model):
    news_id = models.AutoField(primary_key=True)
    part = models.ForeignKey(Department, models.DO_NOTHING)
    news_date = models.DateField()
    title = models.CharField(max_length=20)
    news_content = models.TextField()
    original_content = models.TextField()
    picture_path = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'news'
