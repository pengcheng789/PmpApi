# encoding: utf8

from rest_framework import serializers
from rest_framework.serializers import ValidationError

from .models import Employee, Daily


def md5(string):
    import hashlib
    m = hashlib.md5()
    m.update(string)
    return m.hexdigest()


class LoginSerializer(serializers.HyperlinkedModelSerializer):
    part = serializers.ReadOnlyField(source='part.part_id')

    """
        Over write to_internal_value().
    """
    def to_internal_value(self, data):
        emp_id = data.get('emp_id')
        emp_pass = data.get('emp_pass')
        name = ''

        if not emp_id:
            raise ValidationError({
                'emp_id': '请输入工号！'
            })

        if not emp_pass:
            raise ValidationError({
                'emp_pass': '请输入密码！'
            })

        try:
            employee = Employee.objects.get(emp_id=emp_id)
            name = employee.name
        except:
            raise ValidationError({
                'emp_id': '工号不存在！'
            })

        if md5(emp_pass) != employee.emp_pass:
            raise ValidationError({
                'emp_pass': '密码错误！'
            })

        return {
            'emp_id': emp_id,
            'name': name,
        }

    class Meta:
        model = Employee
        fields = ('emp_id', 'name', 'part', 'sex')
        extra_kwargs = {'emp_pass': {'write_only': True}, }


class DailySerializer(serializers.HyperlinkedModelSerializer):
    part = serializers.ReadOnlyField(source='part.part_id')

    class Meta:
        model = Daily
        fields = ('daily_id', 'part', 'create_date', 'update_date', 'content', 'original_content', 'status')
