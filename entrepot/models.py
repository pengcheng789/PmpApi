# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models

from login.models import Employee


class Commodity(models.Model):
    commodity_id = models.CharField(primary_key=True, max_length=13)
    commodity_name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    count = models.IntegerField()
    unit = models.CharField(max_length=10)
    remark = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'commodity'


class InEntrepot(models.Model):
    ie_id = models.AutoField(primary_key=True)
    ie_date = models.DateField()
    emp = models.ForeignKey(Employee, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'in_entrepot'


class InEntrepotDetail(models.Model):
    id = models.AutoField(primary_key=True)
    ie = models.ForeignKey(InEntrepot, models.DO_NOTHING)
    commodity = models.ForeignKey(Commodity, models.DO_NOTHING)
    ie_count = models.IntegerField()
    unit = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'in_entrepot_detail'
        unique_together = (('ie', 'commodity'),)


class OutEntrepot(models.Model):
    oe_id = models.AutoField(primary_key=True)
    oe_date = models.DateField()
    emp = models.ForeignKey(Employee, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'out_entrepot'


class OutEntrepotDetail(models.Model):
    id = models.AutoField(primary_key=True)
    oe = models.ForeignKey(OutEntrepot, models.DO_NOTHING)
    commodity = models.ForeignKey(Commodity, models.DO_NOTHING)
    oe_count = models.IntegerField()
    unit = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'out_entrepot_detail'
        unique_together = (('oe', 'commodity'),)
