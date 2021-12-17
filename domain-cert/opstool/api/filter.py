import django_filters
from .. import models
class EventFilter(django_filters.FilterSet):
    start = django_filters.DateFromToRangeFilter(field_name='event_start_time', lookup_expr='gte', label='开始时间')
    end = django_filters.DateFromToRangeFilter(field_name='event_end_time', lookup_expr='lte', label='完结时间')
    class Meta:
        model = models.EventRecord
        # exclude = ('active',)
        fields = ["event_name","event_status","event_level","start","end",]


class FaultFilter(django_filters.FilterSet):
    start = django_filters.DateFromToRangeFilter(field_name='fault_start_time', lookup_expr='gte', label='开始时间')
    end = django_filters.DateFromToRangeFilter(field_name='fault_end_time', lookup_expr='lte', label='完结时间')
    class Meta:
        model = models.FaultRecord
        # exclude = ('active',)
        fields = ["fault_name","fault_status","fault_level","start","end",]