# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from time import time

from django.conf import settings

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import jwt 

from .serializers import LoginSerializer, DailySerializer
from .models import Employee, Daily, Department

from tools.auth import check_token

# Create your views here.


class Login(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            employee = Employee.objects.get(emp_id=request.data.get('emp_id'))
            encode = jwt.encode({'emp_id': employee.emp_id,
                                 'auth': employee.auth,
                                 'part_id': employee.part_id,
                                 'create_time': time(),
                                 'ip_addr': request.META.get('REMOTE_ADDR')
                                 },
                                settings.SECRET_KEY, algorithm='HS256')
            token = dict()
            token['token'] = 'JWT ' + encode
            return Response(token)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DailyList(APIView):
    def get(self, request):
        result = check_token(request)
        if not result['permission']:
            return result['response']

        if '1' in result['auth']:
            dailies = Daily.objects.all()
        else:
            try:
                part = Department.objects.get(part_id=result['part_id'])
            except Department.DoesNotExist:
                alert = {'alert': '部门信息有误！'}
                return Response(alert, status=status.HTTP_404_NOT_FOUND)
            dailies = Daily.objects.filter(part=part)

        if not dailies:
            alert = {'alert': '日志信息为空!'}
            return Response(alert)

        serializer = DailySerializer(dailies, many=True)
        return Response(serializer.data)


class DailyDetail(APIView):
    def get(self, request, daily_id):
        result = check_token(request)
        if not result['permission']:
            return result['response']

        if '1' in result['auth']:
            try:
                daily = Daily.objects.get(daily_id=daily_id)
            except Daily.DoesNotExist:
                daily = None
            if daily is None:
                alert = {'alert': '不存在此条日志！'}
                return Response(alert, status=status.HTTP_404_NOT_FOUND)
        else:
            try:
                part = Department.objects.get(part_id=result['part_id'])
            except Department.DoesNotExist:
                alert = {'alert': '部门信息有误！'}
                return Response(alert, status=status.HTTP_404_NOT_FOUND)

            try:
                daily = Daily.objects.get(daily_id=daily_id)
            except Daily.DoesNotExist:
                daily = None

            if daily is None:
                alert = {'alert': '不存在此条日志！'}
                return Response(alert, status=status.HTTP_404_NOT_FOUND)

            if daily.part.id != part.id:
                alert = {'alert': '当前帐号没有权限进行该操作！'}
                return Response(alert, status=status.HTTP_403_FORBIDDEN)

        serializer = DailySerializer(daily)
        return Response(serializer.data)
