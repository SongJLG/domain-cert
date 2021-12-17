from django.urls import path
from . import views

app_name = 'cert'   # 指定命名空间

urlpatterns = [
    path(r'cert', views.CertList.as_view(), name='cert_list'),
    path(r'cert/<pk>', views.CertDetail.as_view(), name='cert_detail'),
]