from django.shortcuts import render
from rest_framework import generics

from applications.brand.models import Brand
from applications.brand.serializers import BrandSerializers


class BrandListView(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializers
