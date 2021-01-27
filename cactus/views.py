from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.viewsets import ModelViewSet

from cactus.models import CactusModel
from cactus.serializers import CactusSerializer


class CactusViewSet(ModelViewSet):
    parser_classes = (MultiPartParser, FormParser,)
    queryset = CactusModel.objects.all()
    serializer_class = CactusSerializer
    lookup_field = 'cactus_id'
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['cactus_name']
    ordering_fields = ['cactus_name']
