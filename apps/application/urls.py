from django.urls import path
from .views import ApplicationCreateView, ApplicationUpdateView, ApplicationListView, MessageCreateView, MessageListView

urlpatterns = [
    path('create/', ApplicationCreateView.as_view(), name='application-create'),
    path('<int:pk>/update/', ApplicationUpdateView.as_view(), name='application-update'),
    path('list/', ApplicationListView.as_view(), name='application-list'),
    path('message/create/', MessageCreateView.as_view(), name='message-create'),
    path('message/list/', MessageListView.as_view(), name='message-list'),
]
