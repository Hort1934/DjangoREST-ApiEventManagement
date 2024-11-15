from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Event, Registration
from .serializers import EventSerializer, RegistrationSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .utils import send_registration_email


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['date', 'location']  # Filter by date and location
    search_fields = ['title', 'description']  # Search by title and description
    ordering_fields = ['date']  # Order by date

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def register(self, request, pk=None):
        event = self.get_object()
        registration, created = Registration.objects.get_or_create(event=event, user=request.user)
        if not created:
            return Response({'detail': 'Already registered for this event.'}, status=status.HTTP_400_BAD_REQUEST)
        # Trigger email notification here after implementing email notification feature.
        return Response(RegistrationSerializer(registration).data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def register(self, request, pk=None):
        event = self.get_object()
        registration, created = Registration.objects.get_or_create(event=event, user=request.user)
        if not created:
            return Response({'detail': 'Already registered for this event.'}, status=status.HTTP_400_BAD_REQUEST)

        # Send the email notification
        send_registration_email(request.user, event)

        return Response(RegistrationSerializer(registration).data, status=status.HTTP_201_CREATED)

