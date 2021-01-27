import uuid

from django.db import models


class CactusModel(models.Model):
    cactus_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cactus_name = models.CharField(max_length=50)
    cactus_picture = models.ImageField(upload_to='pictures', unique=True)

    class Meta:
        db_table = 'cactus'
