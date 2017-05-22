# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Repair
from .serializers import RepairSerializer

from tools.auth import check_token

# Create your views here.


class RepairListView(APIView):

    def get(self, request):
        result = check_token(request)
        if not result['permission']:
            return result['response']

        if all(auth not in result['auth'] for auth in ['1', '10']):
            repairs = Repair.objects.filter(part_id=result['part_id'])

        else:
            repairs = Repair.objects.all()

        if not repairs:
            alert = {'alert': '报修表为空'}
            return Response(alert)

        serializer = RepairSerializer(repairs, many=True)
        return Response(serializer.data)


class RepairDetail(APIView):

    def get_object(self, repair_id):
        try:
            return Repair.objects.get(repair_id=repair_id)
        except Repair.DoesNotExist:
            return None

    def get(self, request, repair_id):
        result = check_token(request)
        if not result['permission']:
            return result['response']

        repair = self.get_object(repair_id)

        if repair is None:
            alert = {'alert': '不存在该保修单！'}
            return Response(alert, status=status.HTTP_404_NOT_FOUND)

        if all(auth not in result['auth'] for auth in ['1', '10']) and repair.part_id != result['part_id']:
            alert = {'alert': '当前帐号没有该操作的权限！'}
            return Response(alert, status=status.HTTP_403_FORBIDDEN)

        serializer = RepairSerializer(repair)
        return Response(serializer.data)



