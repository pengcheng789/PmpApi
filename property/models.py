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


class Repair(models.Model):
    repair_id = models.AutoField(primary_key=True)
    part = models.ForeignKey(Department, models.DO_NOTHING)
    repair_type = models.CharField(max_length=10)
    detail = models.TextField(blank=True, null=True)
    repair_date = models.DateField()
    repair_status = models.CharField(max_length=10)
    send_date = models.DateField()
    follow_date = models.DateField()
    finish_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'repair'
        ordering = ('-send_date', )
