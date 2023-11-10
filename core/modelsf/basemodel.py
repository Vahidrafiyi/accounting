import uuid

from django.db.models           import (Model, DateTimeField, UUIDField, BooleanField)
from django.utils.translation   import gettext_lazy as _

class BaseModel(Model):
    id          = UUIDField(_("id"), primary_key = True, editable = False, default = uuid.uuid4)
    created_at  = DateTimeField(_("created at"), auto_now_add = True)
    is_deleted  = BooleanField(_("is deleted?"), default = False)

    class Meta:
        abstract = True