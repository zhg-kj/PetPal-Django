from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Pet
from .serializers import PetSerializer


class PetCreateView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = PetSerializer


class PetUpdateView(generics.UpdateAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    permission_classes = (IsAuthenticated,)

    def perform_update(self, serializer):
        serializer.save(shelter=self.request.user)


class PetListView(generics.ListAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer

    def get_queryset(self):
        shelter_id = self.request.query_params.get('shelter_id', None)
        if shelter_id:
            return Pet.objects.filter(shelter=shelter_id)
        return Pet.objects.all()
