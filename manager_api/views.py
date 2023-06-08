from django.core.exceptions import ValidationError
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from hardware_api.models import Light

import time

from hardware_api.serializers import LightSerializer


# Create your views here.

class EditLight(APIView):
    """修改灯的状态,前端API"""

    def edit(self, light_id, info):
        try:
            light = Light.objects.get(light_id=light_id)
            light.update(group=info[0], rgb=info[1], edit_flag=True)
            time.sleep(5)
            light = Light.objects.get(light_id=light_id)
            if not light.edit_flag:
                return Response({'success': 'Edit Success'})
            else:
                return Response({'error': 'Edit Failed'})

        except Light.DoesNotExist:
            return Response({'error': 'Light_id does not Exist'})

    def get(self, request, light_id):
        info = [request.GET.get('group'), request.GET.get('rgb')]
        self.edit(light_id, info)
        pass


class GainLightInfo(APIView):
    """获取灯的信息,前端API"""

    def get(self, request, light_id):
        try:
            light = Light.objects.get(light_id=light_id)
            serializer = LightSerializer(light)
            return Response(serializer.data)
        except Light.DoesNotExist:
            return Response({'error': 'Light_id does not Exist'})
        except ValidationError:
            return Response({'error': 'Light_id does not Valid'})
