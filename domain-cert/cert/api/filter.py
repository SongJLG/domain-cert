import django_filters
from .. import models
class CertsFilter(django_filters.FilterSet):
    days = django_filters.NumberFilter(field_name='remain_days', lookup_expr='lte', label='剩余天数')
    class Meta:
        model = models.Certs
        # exclude = ('active',)
        fields = ["name","domain","domain_url","days",]
