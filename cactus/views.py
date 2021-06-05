from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.filters import OrderingFilter
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from cactus.models import CactusModel
from cactus.serializers import CactusSerializer, UserSerializer


class CactusView(ModelViewSet):
    parser_classes = (MultiPartParser, FormParser,)
    queryset = CactusModel.objects.all().order_by('cactus_id')
    serializer_class = CactusSerializer
    lookup_field = 'cactus_id'
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['cactus_name']
    ordering_fields = ['cactus_name']


class UserView(ModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.set_password(instance.password)
        instance.save()

    def perform_update(self, serializer):
        instance = serializer.save()
        instance.set_password(instance.password)
        instance.save()
