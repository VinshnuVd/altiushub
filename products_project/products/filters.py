from django_filters import FilterSet, CharFilter, NumberFilter, DateTimeFilter

class ProductFilter(FilterSet):
    name = CharFilter(lookup_expr='icontains') # Example of explicit filter definition
    address = CharFilter(lookup_expr='icontains') # Example of explicit filter definition
    rent__gt = NumberFilter(field_name='rent', lookup_expr='gt')
    rent__lt = NumberFilter(field_name='rent', lookup_expr='lt')
    no_of_bedrooms = NumberFilter(lookup_expr='exact')
    no_of_bedrooms__gt = NumberFilter(field_name='no_of_bedrooms', lookup_expr='gt')
    posted_on__gte = DateTimeFilter(field_name='posted_on', lookup_expr='gte')