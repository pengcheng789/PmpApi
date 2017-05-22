# encoding:utf8

from datetime import datetime, timedelta

from django.conf import settings

from rest_framework.response import Response
from rest_framework import status

import jwt
from jwt.api_jws import DecodeError


def check_token(request):
    token = get_token(request)
    if token is None:
        alert = {"alert": "请先登录帐号！", }
        return {'permission': False, 'response': Response(alert, status=status.HTTP_401_UNAUTHORIZED)}

    emp_id = decode_token(token, 'emp_id')
    if emp_id is None:
        alert = {"alert": "认证异常，请重新登录！", }
        return {'permission': False, 'response': Response(alert, status=status.HTTP_403_FORBIDDEN)}

    part_id = decode_token(token, 'part_id')
    if part_id is None:
        alert = {"alert": "认证异常，请重新登录！", }
        return {'permission': False, 'response': Response(alert, status=status.HTTP_403_FORBIDDEN)}

    auth_str = decode_token(token, 'auth')
    if auth_str is None:
        alert = {"alert": "认证异常，请重新登录！", }
        return {'permission': False, 'response': Response(alert, status=status.HTTP_403_FORBIDDEN)}

    token_time = decode_token(token, 'create_time')
    if token_time is None:
        alert = {"alert": "认证异常，请重新登录！", }
        return {'permission': False, 'response': Response(alert, status=status.HTTP_403_FORBIDDEN)}
    if datetime.fromtimestamp(token_time) + timedelta(days=1) < datetime.now():
        alert = {"alert": "登录已过期，请重新登录！", }
        return {'permission': False, 'response': Response(alert, status=status.HTTP_403_FORBIDDEN)}

    ip_str = decode_token(token, 'ip_addr')
    if ip_str is None:
        alert = {"alert": "认证异常，请重新登录！", }
        return {'permission': False, 'response': Response(alert, status=status.HTTP_403_FORBIDDEN)}
    if ip_str != request.META.get('REMOTE_ADDR'):
        alert = {"alert": "IP地址已变更，请重新登录！", }
        return {'permission': False, 'response': Response(alert, status=status.HTTP_403_FORBIDDEN)}

    auth_list = auth_str.split(',')
    return {'permission': True, 'emp_id': emp_id, 'part_id': part_id, 'auth': auth_list,
            'token_date': token_time, 'ip_addr': ip_str, }


def get_token(request):
    token = request.META.get('HTTP_AUTHORIZATION')
    if token is not None and len(token) > 4:
        return token[4:]
    return None


def decode_token(token, key):
    try:
        msg = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
    except DecodeError:
        return None
    value = msg.get(key)
    return value
