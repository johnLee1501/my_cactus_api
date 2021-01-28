from django.contrib import admin

from cactus.models import CactusModel


@admin.register(CactusModel)
class CactusAdmin(admin.ModelAdmin):
    """Cactus admin."""

    list_display = ('cactus_name', 'cactus_class', 'cactus_picture', 'cactus_id')
    search_fields = ('cactus_name', 'cactus_class', 'cactus_id')
