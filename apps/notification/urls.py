from django.urls import path
from .views import NotificationCreateView, NotificationListView, NotificationReadView, NotificationDeleteView


urlpatterns = [
    path('create/', NotificationCreateView.as_view(), name='notification-create'),
    path('list/', NotificationListView.as_view(), name='notification-list'),
    path('<int:pk>/read/', NotificationReadView.as_view(), name='notification-read'),
    path('<int:pk>/delete/', NotificationDeleteView.as_view(), name='notification-delete'),
]
