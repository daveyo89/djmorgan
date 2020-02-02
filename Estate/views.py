from rest_framework import permissions, renderers, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from Estate.permissions import IsOwnerOrReadOnly
from Estate.models import Profile, RealEstate
from Estate.serializers import ProfileSerializer, EstateSerializer


class ProfileViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated,
                          IsOwnerOrReadOnly]


class EstateViewSet(viewsets.ModelViewSet):
    queryset = RealEstate.objects.all()
    serializer_class = EstateSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def favorite(self, request, *args, **kwargs):
        estate = self.get_object()
        return Response(estate.favorite)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
