from rest_framework import generics
from .serializers import EventSerializer, FaultSerializer
from ..models import EventRecord, FaultRecord
from .pagination import OpsPageNumberPagination
# from rest_framework.filters import OrderingFilter
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import filter
from .crypt_handler import MyCrypt
import string
import random
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
# from django.contrib.auth.mixins import PermissionRequiredMixin

#@method_decorator(permission_required('opstool.opstool_read_event', login_url=None, raise_exception=True), name='get')
#@method_decorator(permission_required('opstool.opstool_add_event', login_url=None, raise_exception=True), name='post')
class EventList(generics.ListCreateAPIView):
    # permission_required = 'opstool.account_read_add_structure'
    pagination_class = OpsPageNumberPagination
    queryset = EventRecord.objects.all()
    serializer_class = EventSerializer
    ordering = ['id']
    filter_class = filter.EventFilter
    #def get_serializer_class(self):
    #    if self.request.version == "v2":
    #        return 
    #    return EventSerializer

#@method_decorator(permission_required('opstool.opstool_read_event', login_url=None, raise_exception=True), name='get')
#@method_decorator(permission_required('opstool.opstool_update_event', login_url=None, raise_exception=True), name='put')
#@method_decorator(permission_required('opstool.opstool_delete_event', login_url=None, raise_exception=True), name='delete')
class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = EventRecord.objects.all()
    serializer_class = EventSerializer

#@method_decorator(permission_required('opstool.opstool_read_fault', login_url=None, raise_exception=True), name='get')
#@method_decorator(permission_required('opstool.opstool_add_fault', login_url=None, raise_exception=True), name='post')
class FaultList(generics.ListCreateAPIView):
    pagination_class = OpsPageNumberPagination
    queryset = FaultRecord.objects.all()
    serializer_class = FaultSerializer
    ordering = ['id']
    filter_class = filter.FaultFilter

#@method_decorator(permission_required('opstool.opstool_read_fault', login_url=None, raise_exception=True), name='get')
#@method_decorator(permission_required('opstool.opstool_update_fault', login_url=None, raise_exception=True), name='put')
#@method_decorator(permission_required('opstool.opstool_delete_fault', login_url=None, raise_exception=True), name='delete')
class FaultDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FaultRecord.objects.all()
    serializer_class = FaultSerializer


class PasswordView(APIView):
    def get(self, request):
        num = request.GET['num']
        if str(num).isdigit():
            chars = string.ascii_letters + string.digits + "#$%&*!~^"
            random_password = ''.join([random.choice(chars) for i in range(int(num))])
            return Response({'code': 0, 'res': "success", 'msg': random_password}, status=status.HTTP_200_OK)
        else:
            return Response({'code': 1, 'res': "error", 'msg': "请输入正确参数值"}, status=status.HTTP_200_OK)

class CryptView(APIView):
    def get(self, request, *args, **kwargs):
        print(request.user)
        try:
            key = request.GET['key']
            value = request.GET['value']
            if key == 'text':
                if not value:
                    return Response({'code': 0, 'res': "failed", 'msg': "空值没意义"}, status=status.HTTP_200_OK)
                else:
                    encrypt_text = MyCrypt().my_encrypt(value)
                    return Response({'code': 0, 'res': "success", 'msg': encrypt_text}, status=status.HTTP_200_OK)
            elif key == 'ciphertext':
                if not value:
                    return Response({'code': 0, 'res': "failed", 'msg': "空值没意义"}, status=status.HTTP_200_OK)
                else:
                    decrypt_text = MyCrypt().my_decrypt(value)
                    return Response({'code': 0, 'res': "success", 'msg': decrypt_text}, status=status.HTTP_200_OK)
            else:
                return Response({'code': 0, 'res': "failed", 'msg': "参数错误"}, status=status.HTTP_200_OK)
        except:
            return Response({'code': 0, 'res': "failed", 'msg': "参数错误"}, status=status.HTTP_200_OK)

class RSAkeyView(APIView):
    def get(self, requests, *args, **kwargs):
        private_key, public_key = MyCrypt().gen_rsa_key_pair()
        msg = {"private_key": private_key.decode(), "public_key": public_key.decode()}
        # private_key = private_key.decode()
        return Response({'code': 0, 'res': "failed", 'msg': msg}, status=status.HTTP_200_OK)