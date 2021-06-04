from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import SimpleRouter

from cactus.views import CactusViewSet

schema_view = get_schema_view(
    openapi.Info(
        title="My Cactus",
        default_version='v1.0',
        description="My Cactus"
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
router = SimpleRouter()
router.register(r'cactus', CactusViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('', schema_view.with_ui('swagger', cache_timeout=0))
]
