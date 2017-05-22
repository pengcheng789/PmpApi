# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from login.models import Employee
from .models import News, Activity
from .serializers import EmployeeSerializer, NewsSerializer, ActivitySerializer

from tools.auth import check_token

# Create your views here.


class EmployeeList(APIView):

    def get(self, request):
        result = check_token(request)

        if result['permission'] is False:
            return result['response']

        if all(auth not in result['auth'] for auth in ['1', '2', ]):
            alert = {'alert': '当前帐号没有所需操作的权限！'}
            return Response(alert, status=status.HTTP_403_FORBIDDEN)

        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)


class EmployeeDetail(APIView):

    def get_object(self, emp_id):
        try:
            return Employee.objects.get(emp_id=emp_id)
        except Employee.DoesNotExist:
            return None

    def get(self, request, emp_id):
        result = check_token(request)

        if result['permission'] is False:
            return result['response']

        if all(auth not in result['auth'] for auth in ['1', '2', ]) and result['emp_id'] != emp_id:
            alert = {'alert': '当前帐号没有所需操作的权限！'}
            return Response(alert, status=status.HTTP_403_FORBIDDEN)

        employee = self.get_object(emp_id)
        if employee is None:
            alert = {'alert': '不存在此员工信息！'}
            return Response(alert, status=status.HTTP_404_NOT_FOUND)

        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)


class NewsList(APIView):

    def get(self, request):
        result = check_token(request)

        if result['permission'] is False:
            return result['response']

        news = News.objects.all()
        serializer = NewsSerializer(news, many=True)
        return Response(serializer.data)


class NewsDetail(APIView):

    def get_object(self, news_id):
        try:
            return News.objects.get(news_id=news_id)
        except News.DoesNotExist:
            return None

    def get(self, request, news_id):
        result = check_token(request)

        if result['permission'] is False:
            return result['response']

        news = self.get_object(news_id)
        if news is None:
            alert = {'alert': '不存在此条新闻！'}
            return Response(alert, status=status.HTTP_404_NOT_FOUND)

        serializer = NewsSerializer(news)
        return Response(serializer.data)


class ActivityList(APIView):

    def get(self, request):
        result = check_token(request)
        if result['permission'] is False:
            return result['response']

        activities = Activity.objects.all()
        serializer = ActivitySerializer(activities, many=True)
        return Response(serializer.data)


class ActivityDetail(APIView):

    def get_object(self, act_id):
        try:
            return Activity.objects.get(act_id=act_id)
        except Activity.DoesNotExist:
            return None

    def get(self, request, act_id):
        result = check_token(request)

        if result['permission'] is False:
            return result['response']

        activity = self.get_object(act_id)
        if activity is None:
            alert = {'alert': '不存在此活动！'}
            return Response(alert, status=status.HTTP_404_NOT_FOUND)

        serializer = ActivitySerializer(activity)
        return Response(serializer.data)
