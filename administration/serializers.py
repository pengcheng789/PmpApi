from rest_framework import serializers

from login.models import Employee
from .models import News, Activity


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    part = serializers.ReadOnlyField(source='part.part_name')
    room = serializers.ReadOnlyField(source='room.room_id')

    class Meta:
        model = Employee
        fields = ('emp_id', 'name', 'sex', 'part', 'room')


class NewsSerializer(serializers.HyperlinkedModelSerializer):
    part = serializers.ReadOnlyField(source='part.part_name')

    class Meta:
        model = News
        fields = ('news_id', 'part', 'news_date', 'title', 'news_content', 'original_content', 'picture_path', )


class ActivitySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Activity
        fields = ('act_id', 'act_name', 'act_content', 'true_content', )
