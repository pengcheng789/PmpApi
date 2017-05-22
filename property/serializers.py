# encoding: utf8

from rest_framework import serializers

from .models import Repair


class RepairSerializer(serializers.HyperlinkedModelSerializer):
    part = serializers.ReadOnlyField(source='part.part_id')

    class Meta:
        model = Repair
        fields = ('repair_id', 'part', 'repair_type', 'detail', 'repair_date',
                  'repair_status', 'send_date', 'follow_date', 'finish_date')
