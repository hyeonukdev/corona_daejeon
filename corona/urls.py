from django.contrib import admin
from django.urls import path
from main import views as main_views
import certbot_django.server.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_views.main, name="main"),
    # 서버명/patient_admin 주소에서 확진자 동선 추가/삭제 가능.
    path('patient_admin', main_views.patient_admin, name="patient_admin"),
    path('path_add', main_views.path_add, name="path_add"),
    path('path_delete', main_views.path_delete, name="path_delete"),
    path('\.well-known/', certbot_django.server.urls),
]
