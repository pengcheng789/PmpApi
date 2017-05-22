# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models

from administration.models import Activity


class ActMoney(models.Model):
    actmoney_id = models.AutoField(primary_key=True)
    payer_name = models.CharField(max_length=10)
    pay_money = models.IntegerField()
    pay_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'act_money'


class MoneyCount(models.Model):
    mc = models.ForeignKey(ActMoney, models.DO_NOTHING)
    act = models.ForeignKey(Activity, models.DO_NOTHING)
    money_count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'money_count'
        unique_together = (('mc', 'act'),)
