from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Event, Registration
from .serializers import EventSerializer, RegistrationSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework import generics


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def register(self, request, pk=None):
        event = self.get_object()
        registration, created = Registration.objects.get_or_create(event=event, user=request.user)
        if not created:
            return Response({'detail': 'Already registered for this event.'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(RegistrationSerializer(registration).data, status=status.HTTP_201_CREATED)
