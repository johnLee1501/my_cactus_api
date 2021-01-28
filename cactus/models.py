import uuid

from django.db import models


class CactusModel(models.Model):
    cactus_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cactus_name = models.CharField(max_length=50)
    cactus_class = models.CharField(max_length=50, null=True, blank=True)
    cactus_description = models.TextField(max_length=200, null=True, blank=True)
    cactus_picture = models.ImageField(upload_to='pictures', unique=True)

    class Meta:
        db_table = 'cactus'

    def __str__(self):
        return self.cactus_name
