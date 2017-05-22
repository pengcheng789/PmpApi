# encoding: utf8

from rest_framework import serializers

from .models import Car
from login.models import Room, TempEmployee


class RoomSerializer(serializers.HyperlinkedModelSerializer):
    # employees = serializers.HyperlinkedRelatedField(many=True, view_name='employee-detail',
    #                                                read_only=True)

    class Meta:
        model = Room
        fields = ('room_id', 'beds', )


class CarSerializer(serializers.HyperlinkedModelSerializer):
    act_name = serializers.ReadOnlyField(source='act.act_name')

    class Meta:
        model = Car
        fields = ('car_id', 'car_status', 'act_name')


class TempEmployeeSerializer(serializers.HyperlinkedModelSerializer):
    part_name = serializers.ReadOnlyField(source='part.part_name')
    room_id = serializers.ReadOnlyField(source='room.room_id')

    class Meta:
        model = TempEmployee
        fields = ('emp_id', 'name', 'sex', 'job', 'adress', 'part_name',
                  'in_date', 'child_yn', 'room_id', 'date_count', 'id_card',
                  'out_date', 'remark', )
