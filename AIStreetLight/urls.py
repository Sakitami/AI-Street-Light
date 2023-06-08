from django.contrib import admin
from django.urls import path
from rest_framework.documentation import include_docs_urls

from hardware_api.views import LightStatusUpload, LightStatusDownload
from manager_api.views import EditLight, GainLightInfo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('light/post/<light_id>/', LightStatusUpload.as_view(), name='light_status_upload'),
    path('light/get/<light_id>/', LightStatusDownload.as_view(), name='light_status_download'),
    path('manager/edit/<light_id>/', EditLight.as_view(), name='light_status_edit'),
    path('manager/info/<light_id>/', GainLightInfo.as_view(), name='light_info'),
    # path('docs/', include_docs_urls(title='AIStreetLight API')),
]
