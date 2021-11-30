from django.urls import path
from applications.clothes.views import ClothesListView, ClothesDetailView

urlpatterns = [
    path('clothes-list/', ClothesListView.as_view()),
    path('clothes-list/<int:pk>/', ClothesDetailView.as_view()),
]
