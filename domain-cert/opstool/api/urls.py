from django.urls import path
from . import views

app_name = 'opstool'   # 指定命名空间

urlpatterns = [
    path(r'opstool/event', views.EventList.as_view(), name='event_list'),
    path(r'opstool/event/<pk>', views.EventDetail.as_view(), name='event_detail'),
    path(r'opstool/fault', views.FaultList.as_view(), name='fault_list'),
    path(r'opstool/fault/<pk>', views.FaultDetail.as_view(), name='fault_detail'),
    path(r'opstool/password', views.PasswordView.as_view(), name='password'),
    path(r'opstool/crypt', views.CryptView.as_view(), name='crypt'),
    path(r'opstool/rsakey', views.RSAkeyView.as_view(), name='rsakey'),
]