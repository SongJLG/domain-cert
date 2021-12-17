from rest_framework import serializers, validators
from ..models import Certs

class CertSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=45, label="域名名称", help_text='填写域名对应的服务',
                                 validators=[validators.UniqueValidator(queryset=Certs.objects.all(), message="事件名字段必须唯一")])

    id = serializers.UUIDField(read_only=True)
   # orther_domain = serializers.CharField(read_only=True)
   # organization_name = serializers.CharField(read_only=True)
   # serial_number = serializers.CharField(read_only=True)
   # issued_by = serializers.CharField(read_only=True)
   # cert_type = serializers.CharField(read_only=True)
   # notbefore = serializers.CharField(read_only=True)
   # notafter = serializers.CharField(read_only=True)
   # remain_days = serializers.IntegerField(read_only=True)

    class Meta:
        model = Certs
        fields = '__all__' 
        # fields = ('id', 'title', 'content', 'last_modify_date', 'created')

# class   CertSerializerV2(serializers.Serializer):
