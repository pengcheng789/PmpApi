# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import (Commodity, InEntrepot, InEntrepotDetail,
                     OutEntrepot, OutEntrepotDetail)
from .serializers import (CommoditySerializer,
                          InEntrepotSerializer, InEntrepotDetailSerializer,
                          OutEntrepotSerializer, OutEntrepotDetailSerializer)

from tools.auth import check_token

# Create your views here.


class CommodityList(APIView):
    def get(self, request):
        result = check_token(request)
        if result['permission'] is False:
            return result['response']

        if all(auth not in result['auth'] for auth in ['1', '11', ]):
            alert = {'alert': '当前帐号没有所需操作的权限！'}
            return Response(alert, status=status.HTTP_403_FORBIDDEN)

        commodities = Commodity.objects.all()
        if commodities is False:
            alert = {'alert': '商品表为空'}
            return Response(alert)
        serializer = CommoditySerializer(commodities, many=True)

        return Response(serializer.data)


class CommodityDetail(APIView):
    def get_object(self, commodity_id):
        try:
            return Commodity.objects.get(commodity_id=commodity_id)
        except Commodity.DoesNotExist:
            return None

    def get(self, request, commodity_id):
        result = check_token(request)
        if result['permission'] is False:
            return result['response']

        if all(auth not in result['auth'] for auth in ['1', '11', ]):
            alert = {'alert': '当前帐号没有所需操作的权限！'}
            return Response(alert, status=status.HTTP_403_FORBIDDEN)

        commodity = self.get_object(commodity_id)
        if commodity is None:
            alert = {'alert': '不存在此商品信息！'}
            return Response(alert, status=status.HTTP_404_NOT_FOUND)

        serializer = CommoditySerializer(commodity)
        return Response(serializer.data)


class InEntrepotList(APIView):
    def get(self, request):
        result = check_token(request)
        if result['permission'] is False:
            return result['response']

        if all(auth not in result['auth'] for auth in ['1', '11', ]):
            alert = {'alert': '当前帐号没有所需操作的权限！'}
            return Response(alert, status=status.HTTP_403_FORBIDDEN)

        in_entrepots = InEntrepot.objects.all()
        if in_entrepots is False:
            alert = {'alert': '入库表为空'}
            return Response(alert)
        serializer = InEntrepotSerializer(in_entrepots, many=True)

        return Response(serializer.data)


class InEntrepotDetailView(APIView):
    def get_object_list(self, ie_id):
        return InEntrepotDetail.objects.filter(ie_id=ie_id)

    def get(self, request, ie_id):
        result = check_token(request)
        if result['permission'] is False:
            return result['response']

        if all(auth not in result['auth'] for auth in ['1', '11', ]):
            alert = {'alert': '当前帐号没有所需操作的权限！'}
            return Response(alert, status=status.HTTP_403_FORBIDDEN)

        in_entrepot_detail_list = self.get_object_list(ie_id)
        if not in_entrepot_detail_list:
            try:
                in_entrepot = InEntrepot.objects.get(ie_id=ie_id)
            except InEntrepot.DoesNotExist:
                alert = {'alert': '不存在此入库单！'}
                return Response(alert, status=status.HTTP_404_NOT_FOUND)

            serializer = InEntrepotSerializer(in_entrepot)
            return Response(serializer.data)

        serializer = InEntrepotDetailSerializer(in_entrepot_detail_list, many=True)
        return Response(serializer.data)


class OutEntrepotList(APIView):
    def get(self, request):
        result = check_token(request)
        if result['permission'] is False:
            return result['response']

        if all(auth not in result['auth'] for auth in ['1', '11', ]):
            alert = {'alert': '当前帐号没有所需操作的权限！'}
            return Response(alert, status=status.HTTP_403_FORBIDDEN)

        out_entrepots = OutEntrepot.objects.all()
        if out_entrepots is False:
            alert = {'alert': '出库为空'}
            return Response(alert)
        serializer = InEntrepotSerializer(out_entrepots, many=True)

        return Response(serializer.data)


class OutEntrepotDetailView(APIView):
    def get_object_list(self, oe_id):
        return OutEntrepotDetail.objects.filter(oe_id=oe_id)

    def get(self, request, oe_id):
        result = check_token(request)
        if result['permission'] is False:
            return result['response']

        if all(auth not in result['auth'] for auth in ['1', '11', ]):
            alert = {'alert': '当前帐号没有所需操作的权限！'}
            return Response(alert, status=status.HTTP_403_FORBIDDEN)

        out_entrepot_detail_list = self.get_object_list(oe_id)
        if not out_entrepot_detail_list:
            try:
                out_entrepot = OutEntrepot.objects.get(oe_id=oe_id)
            except OutEntrepot.DoesNotExist:
                alert = {'alert': '不存在此出库单！'}
                return Response(alert, status=status.HTTP_404_NOT_FOUND)

            serializer = OutEntrepotSerializer(out_entrepot)
            return Response(serializer.data)

        serializer = OutEntrepotDetailSerializer(out_entrepot_detail_list, many=True)
        return Response(serializer.data)
