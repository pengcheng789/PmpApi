# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Car
from login.models import Room, TempEmployee
from .serializers import CarSerializer, RoomSerializer, TempEmployeeSerializer

from tools.auth import check_token

# Create your views here.


class RoomList(APIView):
    def get(self, request):
        result = check_token(request)
        if not result['permission']:
            return result['response']

        if all(auth not in result['auth'] for auth in ['1', '8']):
            alert = {'alert': '当前帐号没有权限进行该操作！'}
            return Response(alert, status=status.HTTP_403_FORBIDDEN)

        rooms = Room.objects.all()
        if not rooms:
            alert = {'alert': '当前房间表为空！'}
            return Response(alert)

        serializer = RoomSerializer(rooms, many=True)
        return Response(serializer.data)


class RoomDetail(APIView):

    def get_object(self, room_id):
        try:
            return Room.objects.get(room_id=room_id)
        except Room.DoesNotExist:
            return None

    def get(self, request, room_id):
        result = check_token(request)
        if not result['permission']:
            return result['response']

        if all(auth not in result['auth'] for auth in ['1', '8']):
            alert = {'alert': '当前帐号没有权限进行该操作！'}
            return Response(alert, status=status.HTTP_403_FORBIDDEN)

        room = self.get_object(room_id)
        if room is None:
            alert = {'alert': '不存在该房间信息！'}
            return Response(alert, status=status.HTTP_404_NOT_FOUND)

        serializer = RoomSerializer(room)
        return Response(serializer.data)


class CarList(APIView):
    def get(self, request):
        result = check_token(request)
        if not result['permission']:
            return result['response']

        if all(auth not in result['auth'] for auth in ['1', '8']):
            alert = {'alert': '当前帐号没有权限进行该操作！'}
            return Response(alert, status=status.HTTP_403_FORBIDDEN)

        cars = Car.objects.all()
        if not cars:
            alert = {'alert': '当前车队表为空！'}
            return Response(alert)

        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)


class CarDetail(APIView):

    def get_object(self, car_id):
        try:
            return Car.objects.get(car_id=car_id)
        except Car.DoesNotExist:
            return None

    def get(self, request, car_id):
        result = check_token(request)
        if not result['permission']:
            return result['response']

        if all(auth not in result['auth'] for auth in ['1', '8']):
            alert = {'alert': '当前帐号没有权限进行该操作！'}
            return Response(alert, status=status.HTTP_403_FORBIDDEN)

        car = self.get_object(car_id)
        if car is None:
            alert = {'alert': '不存在该车信息！'}
            return Response(alert, status=status.HTTP_404_NOT_FOUND)

        serializer = CarSerializer(car)
        return Response(serializer.data)


class TempEmployeeList(APIView):
    def get(self, request):
        result = check_token(request)
        if not result['permission']:
            return result['response']

        if all(auth not in result['auth'] for auth in ['1', '8']):
            alert = {'alert': '当前帐号没有权限进行该操作！'}
            return Response(alert, status=status.HTTP_403_FORBIDDEN)

        temp_employees = TempEmployee.objects.all()
        if not temp_employees:
            alert = {'alert': '当前义工表为空！'}
            return Response(alert)

        serializer = TempEmployeeSerializer(temp_employees, many=True)
        return Response(serializer.data)


class TempEmployeeDetail(APIView):

    def get_object(self, temp_emp_id):
        try:
            return TempEmployee.objects.get(emp_id=temp_emp_id)
        except TempEmployee.DoesNotExist:
            return None

    def get(self, request, temp_emp_id):
        result = check_token(request)
        if not result['permission']:
            return result['response']

        if all(auth not in result['auth'] for auth in ['1', '8']):
            alert = {'alert': '当前帐号没有权限进行该操作！'}
            return Response(alert, status=status.HTTP_403_FORBIDDEN)

        temp_employee = self.get_object(temp_emp_id)
        if temp_employee is None:
            alert = {'alert': '不存在该义工信息！'}
            return Response(alert, status=status.HTTP_404_NOT_FOUND)

        serializer = TempEmployeeSerializer(temp_employee)
        return Response(serializer.data)
