from django.urls import path
from .views import PetCreateView, PetUpdateView, PetListView

urlpatterns = [
    path('create/', PetCreateView.as_view(), name='pet-create'),
    path('<int:pk>/update/', PetUpdateView.as_view(), name='pet-update'),
    path('list/', PetListView.as_view(), name='pet-list'),
]
