# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Room(models.Model):
    room_id = models.CharField(primary_key=True, max_length=10)
    beds = models.IntegerField()

    def __unicode__(self):
            return self.room_id

    class Meta:
        managed = False
        db_table = 'room'


class Daily(models.Model):
    daily_id = models.AutoField(primary_key=True)
    part = models.ForeignKey('Department', models.DO_NOTHING)
    create_date = models.DateField()
    update_date = models.DateField()
    content = models.TextField()
    original_content = models.TextField(default='')
    status = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'daily'
        ordering = ('-create_date', )


class Department(models.Model):
    part_id = models.CharField(primary_key=True, max_length=10)
    part_name = models.CharField(max_length=10)
    admin = models.ForeignKey('Employee', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'department'


class Employee(models.Model):
    emp_id = models.CharField(primary_key=True, max_length=20)
    emp_pass = models.CharField(max_length=100)
    auth = models.CharField(max_length=100)
    name = models.CharField(max_length=10)
    sex = models.CharField(max_length=2)
    part = models.ForeignKey(Department, models.DO_NOTHING)
    room = models.ForeignKey('Room', related_name='employees', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee'


class TempEmployee(models.Model):
    emp_id = models.CharField(primary_key=True, max_length=20)
    emp_pass = models.CharField(max_length=100)
    name = models.CharField(max_length=10)
    sex = models.CharField(max_length=2)
    job = models.CharField(max_length=100)
    adress = models.CharField(max_length=100)
    part = models.ForeignKey(Department, models.DO_NOTHING)
    in_date = models.DateField()
    child_yn = models.CharField(max_length=2)
    room = models.ForeignKey(Room, models.DO_NOTHING, blank=True, null=True)
    date_count = models.SmallIntegerField()
    id_card = models.CharField(max_length=20)
    out_date = models.DateField()
    remark = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'temp_employee'
