from django.urls import path
from .views import UserLoginView, UserRegisterView, TokenRefreshView, UserDetailsView, UserUpdateView, UserDeleteView

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('register/', UserRegisterView.as_view(), name='user-register'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('details/', UserDetailsView.as_view(), name='user-details'),
    path('update/', UserUpdateView.as_view(), name='user-update'),
    path('delete/', UserDeleteView.as_view(), name='user-delete'),
]
