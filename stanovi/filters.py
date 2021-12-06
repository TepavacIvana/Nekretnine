from django_filters import rest_framework as filters
from .models import Stan


class StanByFilters(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')
    district = filters.CharFilter(field_name='district', lookup_expr='icontains')
    size = filters.CharFilter(field_name='size', lookup_expr='exact')
    num_of_rooms = filters.NumberFilter(field_name='num_of_rooms', lookup_expr='icontains')
    available = filters.BooleanFilter(field_name='available')
    reserved = filters.BooleanFilter(field_name='reserved')
    sold = filters.BooleanFilter(field_name='sold')

    class Meta:
        model = Stan
        fields = ['min_price', 'max_price', 'district', 'size', 'num_of_rooms', 'available', 'reserved', 'sold']
