from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import TokenObtainPairSerializer, UserSerializer, RoleSerializer, StructureSerializer, UserDetailSerializer, UsernameSerializer
from ..models import User, Role, Structure
from rest_framework import generics
from rest_framework.views import APIView
from .perms import PermsManage
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
from rest_framework.filters import SearchFilter


class TokenObtainPairView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer


@method_decorator(permission_required('account.account_read_user', login_url=None, raise_exception=True), name='get')
@method_decorator(permission_required('account.account_add_user', login_url=None, raise_exception=True), name='post')
class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    ordering = ['id']

@method_decorator(permission_required('account.account_read_user', login_url=None, raise_exception=True), name='get')
@method_decorator(permission_required('account.account_change_user', login_url=None, raise_exception=True), name='put')
@method_decorator(permission_required('account.account_delete_user', login_url=None, raise_exception=True), name='delete')
class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@method_decorator(permission_required('account.account_read_role', login_url=None, raise_exception=True), name='get')
@method_decorator(permission_required('account.account_add_role', login_url=None, raise_exception=True), name='post')
class RoleListView(generics.ListCreateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    ordering = ['id']


@method_decorator(permission_required('account.account_read_role', login_url=None, raise_exception=True), name='get')
@method_decorator(permission_required('account.account_change_role', login_url=None, raise_exception=True), name='put')
@method_decorator(permission_required('account.account_delete_role', login_url=None, raise_exception=True), name='delete')
class RoleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


@method_decorator(permission_required('account.account_read_structure', login_url=None, raise_exception=True), name='get')
@method_decorator(permission_required('account.account_add_structure', login_url=None, raise_exception=True), name='post')
class StructureListView(generics.ListCreateAPIView):
    queryset = Structure.objects.all()
    serializer_class = StructureSerializer
    ordering = ['id']


@method_decorator(permission_required('account.account_read_structure', login_url=None, raise_exception=True), name='get')
@method_decorator(permission_required('account.account_change_structure', login_url=None, raise_exception=True), name='put')
@method_decorator(permission_required('account.account_delete_structure', login_url=None, raise_exception=True), name='delete')
class StructureDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Structure.objects.all()
    serializer_class = StructureSerializer


class PermsView(APIView):
    def get(self, request, *args, **kwargs):
       # filter_backends = [SearchFilter,]
       # search_fields = ('name',)
        perms_list = PermsManage().get_perms()
        return Response({'code': 0, 'res': "success", 'msg': perms_list}, status=status.HTTP_200_OK)

class UsernameView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UsernameSerializer
    ordering = ['id']
    filter_backends = [SearchFilter,]
    search_fields = ('name',)



class ChangePasswd(APIView):
    def post(self, request, *args, **kwargs):
        user = request.user
        if user.id != request.user.id and request.user.is_superuser is False:return "您无权操作此项"  
             
        elif user.id == request.user.id or request.user.is_superuser:
            if request.POST.get('password') == request.POST.get('c_password'):
                try:                 
                    user.set_password(request.POST.get('password'))
                    user.save()
                    return True
                except Exception as ex:
                    return "密码修改失败：%s" % str(ex) 
        return "修改密码失败"

class UserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserDetailSerializer
    queryset = User.objects.all()
    def get_object(self):
        return self.request.user
    
    
