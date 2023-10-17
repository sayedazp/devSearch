from django.db import models
import uuid

class Base_model(models.Model):
    class Meta:
        abstract = True
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
