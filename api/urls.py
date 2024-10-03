from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenBlacklistView
from .views import FindAnimalsView, NewsListView, AnimalOptionsView, UserCreateView

urlpatterns = [
    path('animals/', FindAnimalsView.as_view()),
    path('animal-options/', AnimalOptionsView.as_view()),
    path('news/', NewsListView.as_view()),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # This is basically the logout:
    path('token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),
    path('register/', UserCreateView.as_view(), name='api_register'),
]