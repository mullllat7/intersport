from django.urls import path
from applications.brand.views import BrandListView

urlpatterns = [
    path('brand-list/', BrandListView.as_view()),
]