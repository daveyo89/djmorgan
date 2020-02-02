from rest_framework import permissions, viewsets
from Estate.permissions import IsOwnerOrReadOnly, IsMyLike
from Estate.models import Profile, RealEstate, Liked
from Estate.serializers import ProfileSerializer, EstateSerializer, LikedSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [
        permissions.IsAuthenticated, IsOwnerOrReadOnly
    ]


class EstateViewSet(viewsets.ModelViewSet):
    queryset = RealEstate.objects.all()
    serializer_class = EstateSerializer
    permission_classes = [
        permissions.IsAuthenticated, IsOwnerOrReadOnly
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LikedViewSet(viewsets.ModelViewSet):
    queryset = Liked.objects.all()
    serializer_class = LikedSerializer
    permission_classes = [
        permissions.IsAuthenticated, IsMyLike
    ]
