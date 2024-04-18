import uuid
from django.db import models


class AbstractBaseModel(models.Model):
    """
    Base abstract model with created_at and updated_at fields, and uuid as id.
    """

    id = models.UUIDField(
        "UUID", primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    created_at = models.DateTimeField("created at", auto_now_add=True)
    updated_at = models.DateTimeField("updated at", auto_now=True)

    class Meta:
        abstract = True
        ordering = ["-created_at"]

    def __repr__(self):
        return f"<{self.__class__.__name__} {self.uuid}>"
