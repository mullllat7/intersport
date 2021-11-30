from django.shortcuts import render
from django_filters import rest_framework

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from applications.clothes.models import Clothes
from applications.clothes.serializers import ClothesSerializer, ClothesDetailSerializer
from rest_framework.decorators import action


class ClothesPriceFilter(rest_framework.FilterSet):

    min_price = rest_framework.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = rest_framework.NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Clothes
        fields = [
            'brand',
            'min_price',
            'max_price',
        ]


class ClothesListView(generics.ListAPIView):

    queryset = Clothes.objects.all()
    serializer_class = ClothesSerializer
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filter_class = ClothesPriceFilter
    search_fields = ['title', ]

    def get_serializer_context(self):
        return {'request': self.request}


class ClothesDetailView(generics.RetrieveAPIView):
    queryset = Clothes.objects.all()
    serializer_class = ClothesDetailSerializer


class ClothesViewSet(viewsets.ModelViewSet):
    queryset = Clothes.objects.all()
    serializer_class = ClothesSerializer
    permission_classes = [IsAuthenticated, ]

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permissions = []
        elif self.action == 'saved':
            permissions = [IsAuthenticated, ]
        else:
            permissions = [IsClothesAuthor, ]
        return [permissions() for permissions in permissions]

    def get_serializer_context(self):
        return {'request': self.request}