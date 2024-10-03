from django.urls import path
from .views import (
    AnimalListView,
    AnimalDetailView, 
    AnimalCreateView,
    AnimalUpdateView,
    AnimalDeleteView
)

urlpatterns = [
    path('', AnimalListView.as_view(), name='animals-list'),
    path('<int:pk>/', AnimalDetailView.as_view(), name='animals-detail'),
    path('new/', AnimalCreateView.as_view(), name='animals-create'),
    path('<int:pk>/update/', AnimalUpdateView.as_view(), name='animal-update'),
    path('<int:pk>/delete/', AnimalDeleteView.as_view(), name='animal-delete')
]