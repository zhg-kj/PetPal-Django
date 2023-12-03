from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Application, Message
from .serializers import ApplicationSerializer, MessageSerializer


class ApplicationCreateView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ApplicationSerializer


class ShelterUserOnlyPermission(IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        return obj.shelter == request.user and not request.user.is_seeker


class ApplicationUpdateView(generics.UpdateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = (ShelterUserOnlyPermission,)


class ApplicationListView(generics.ListAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return Application.objects.filter(seeker=user) | Application.objects.filter(shelter=user)


class MessageCreateView(generics.CreateAPIView):
    serializer_class = MessageSerializer
    permission_classes = (IsAuthenticated,)


class MessageListView(generics.ListAPIView):
    serializer_class = MessageSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        application_id = self.request.query_params.get('application_id')
        print(application_id)
        return Message.objects.filter(application=application_id)
