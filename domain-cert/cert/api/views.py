from rest_framework import generics
from .serializers import CertSerializer
from ..models import Certs
from .pagination import MyPageNumberPagination
from .filter import CertsFilter
# from rest_framework.filters import OrderingFilter
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator

#@method_decorator(permission_required('cert.cert_read', login_url=None, raise_exception=True), name='get')
#@method_decorator(permission_required('cert.cert_add', login_url=None, raise_exception=True), name='post')
class CertList(generics.ListCreateAPIView):
    # print(request.user)
    pagination_class = MyPageNumberPagination
    queryset = Certs.objects.all()
    serializer_class = CertSerializer
    ordering = ['name']
    filter_class = CertsFilter


#@method_decorator(permission_required('cert.cert_read', login_url=None, raise_exception=True), name='get')
#@method_decorator(permission_required('cert.cert_update', login_url=None, raise_exception=True), name='put')
#@method_decorator(permission_required('cert.cert_delete', login_url=None, raise_exception=True), name='delete')
class CertDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Certs.objects.all()
    serializer_class = CertSerializer