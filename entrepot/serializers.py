from rest_framework import serializers

from .models import (Commodity, InEntrepot, InEntrepotDetail,
                     OutEntrepot, OutEntrepotDetail)


class CommoditySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Commodity
        fields = ('commodity_id', 'commodity_name', 'type', 'count', 'unit', 'remark')


class InEntrepotSerializer(serializers.HyperlinkedModelSerializer):
    emp_id = serializers.ReadOnlyField(source='emp.emp_id')
    emp_name = serializers.ReadOnlyField(source='emp.name')

    class Meta:
        model = InEntrepot
        fields = ('ie_id', 'ie_date', 'emp_id', 'emp_name')


class InEntrepotDetailSerializer(serializers.HyperlinkedModelSerializer):
    ie_id = serializers.ReadOnlyField(source='ie.ie_id')
    commodity = serializers.ReadOnlyField(source='commodity.commodity_name')
    ie_date = serializers.ReadOnlyField(source='ie.ie_date')
    emp_id = serializers.ReadOnlyField(source='ie.emp.emp_id')
    emp_name = serializers.ReadOnlyField(source='ie.emp.name')

    class Meta:
        model = InEntrepotDetail
        fields = ('id', 'ie_id', 'commodity', 'ie_count', 'unit', 'ie_date', 'emp_id', 'emp_name')


class OutEntrepotSerializer(serializers.HyperlinkedModelSerializer):
    emp = serializers.ReadOnlyField(source='emp.emp_id')
    emp_name = serializers.ReadOnlyField(source='emp.name')

    class Meta:
        model = OutEntrepot
        fields = ('oe_id', 'oe_date', 'emp', 'emp_name')


class OutEntrepotDetailSerializer(serializers.HyperlinkedModelSerializer):
    oe_id = serializers.ReadOnlyField(source='oe.oe_id')
    commodity = serializers.ReadOnlyField(source='commodity.commodity_name')
    oe_date = serializers.ReadOnlyField(source='oe.oe_date')
    emp_id = serializers.ReadOnlyField(source='oe.emp.emp_id')
    emp_name = serializers.ReadOnlyField(source='oe.emp.name')

    class Meta:
        model = OutEntrepotDetail
        fields = ('id', 'oe_id', 'commodity', 'oe_count', 'unit', 'oe_date', 'emp_id', 'emp_name')
