from django.core.exceptions import ValidationError
from django.http import Http404
from django.shortcuts import render
from rest_framework.views import APIView

from .models import Light
from .serializers import LightSerializer, LightStatusDown, LightStatusUp

from rest_framework.response import Response

import time


class LightStatusUpload(APIView):
    """上传当前灯的状态，路灯API"""

    def post(self, request, light_id):
        light = Light.objects.get(light_id=light_id)
        serializer = LightStatusUp(light, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': 'Data Upload Success'})
        return Response(serializer.errors)


class LightStatusDownload(APIView):
    """下载当前灯的状态,路灯API"""

    def get_object(self, light_id):
        try:
            light = Light.objects.get(light_id=light_id)
            return light
        except Light.DoesNotExist:
            Response({'error': 'Light_id does not Exist'})

    def get(self, request, light_id):
        light = self.get_object(light_id)
        if light.edit_flag:
            serializer = LightStatusDown(light)
            light.update(edit_flag=False)
            return Response(serializer.data)
        return Response({'info': 'No Exchange'})


# class EditLight(APIView):
#     """修改灯的状态,前端API"""
#
#     def edit(self, light_id, info):
#         try:
#             light = Light.objects.get(light_id=light_id)
#             light.update(group=info[0], rgb=info[1], edit_flag=True)
#             time.sleep(5)
#             light = Light.objects.get(light_id=light_id)
#             if not light.edit_flag:
#                 return Response({'success': 'Edit Success'})
#             else:
#                 return Response({'error': 'Edit Failed'})
#
#         except Light.DoesNotExist:
#             return Response({'error': 'Light_id does not Exist'})
#
#     def get(self, request, light_id):
#         info = [request.GET.get('group'), request.GET.get('rgb')]
#         self.edit(light_id, info)
#         pass
#
#
# class GainLightInfo(APIView):
#     """获取灯的信息,前端API"""
#
#     def get(self, request, light_id):
#         try:
#             light = Light.objects.get(light_id=light_id)
#             serializer = LightSerializer(light)
#             return Response(serializer.data)
#         except Light.DoesNotExist:
#             return Response({'error': 'Light_id does not Exist'})
#         except ValidationError:
#             return Response({'error': 'Light_id does not Valid'})
