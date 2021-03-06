from django_filters import rest_framework as filters
from .models import Ponuda


class PonudaByFilters(filters.FilterSet):
    start_date = filters.DateFilter(field_name='contract_date', lookup_expr='gte')
    end_date = filters.DateFilter(field_name='contract_date', lookup_expr='lte')
    date_range = filters.DateRangeFilter(field_name='contract_date')
    prodaja_detail = filters.CharFilter(field_name='prodaja_detail', lookup_expr='icontains')
    sales_status = filters.CharFilter(field_name='sales_status', lookup_expr='icontains')

    class Meta:
        model = Ponuda
        fields = ['start_date', 'end_date', 'date_range', 'prodaja_detail', 'sales_status']
