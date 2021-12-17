# simple/serializers.py
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from ..models import User, Role, Structure


class TokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        data['username'] = self.user.username
        return data


class UserSerializer(serializers.ModelSerializer):
    last_login = serializers.DateTimeField(read_only=True)
    date_joined = serializers.DateTimeField(read_only=True)
    class Meta:
        model = User
        # fields = '__all__'
        exclude = ('first_name' , 'last_name', 'is_staff',)

   # def create(self, validated_data):
   #     user = super(UserSerializer, self).create(validated_data=validated_data)
   #     user.set_password(validated_data["password"])
   #     user.save()
   #     return user

class UsernameSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'name',)

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'email', 'mobile']

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'


class StructureSerializer(serializers.ModelSerializer):
#    user_name = serializers.SerializerMethodField()
#    class Meta:
#        model = Structure
#        fields = ['text', 'desc', 'type', 'manage', 'parent', "user_name"]
#
#    @staticmethod
#    def get_user_name(obj):
#        user = User.objects.filter(id=obj.manage)
#        if user:
#            return user.name
#        else:
#            return '--'
    paths = serializers.SerializerMethodField(read_only=True,required=False)
    last_node = serializers.SerializerMethodField(read_only=True,required=False) 
    manage_name = serializers.SerializerMethodField(read_only=True,required=False)    
    class Meta:
        model = Structure
        fields = ('id','text','desc', 'type', 'parent', 'mail_group','manage','manage_name','wechat_webhook_url', 'dingding_webhook_url', 'paths','last_node','tree_id')     
           
    def get_paths(self,obj):
        return obj.node_path()
    
    def get_last_node(self,obj):
        return obj.last_node()
    
    def get_manage_name(self,obj):
        return obj.manage_name()   

