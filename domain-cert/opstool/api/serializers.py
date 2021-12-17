from rest_framework import serializers, validators
from ..models import EventRecord, FaultRecord

class EventSerializer(serializers.ModelSerializer):
    event_name = serializers.CharField(max_length=45, label="事件名称", help_text='事件名称',
                                       validators=[validators.UniqueValidator(queryset=EventRecord.objects.all(), message="事件名字段必须唯一")])

    class Meta:
        model = EventRecord
        fields = '__all__' 
        # fields = ('id', 'title', 'content', 'last_modify_date', 'created')

class FaultSerializer(serializers.ModelSerializer):
    fault_name = serializers.CharField(max_length=45, label="故障名称", help_text='故障名称,不要重复填写',
                                       validators=[validators.UniqueValidator(queryset=FaultRecord.objects.all(), message="故障名字段必须唯一")])

    class Meta:
        model = FaultRecord
        fields = '__all__' 
