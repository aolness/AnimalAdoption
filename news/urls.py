from django.urls import path
from .views import (
    NewsDetailView,
    NewsListView,
    NewsCreateView,
    NewsUpdateView,
    NewsDeleteView
)

urlpatterns = [
    path('', NewsListView.as_view(), name='news-list'),
    path('<int:pk>/', NewsDetailView.as_view(), name='news-detail'),
    path('new/', NewsCreateView.as_view(), name='news-create'),
    path('update/<int:pk>/', NewsUpdateView.as_view(), name='news-update'),
    path('delete/<int:pk>/', NewsDeleteView.as_view(), name='news-delete')
]
