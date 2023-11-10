from django.db.models           import (ForeignKey, CASCADE, CharField, TextField)
from django.utils.translation   import gettext_lazy as _

from .basemodel                 import BaseModel
from core.models                import User


class SubjectCategory(BaseModel):
    owner         = ForeignKey(verbose_name = _("owner"), to = User, on_delete = CASCADE)
    title         = CharField(_("title"),       max_length = 200)           
    description   = TextField(_("description"), max_length = 1000, null = True, blank = True) 

    class Meta:
        ordering            = ['-title']
        verbose_name_plural = 'subject categories'

    def __str__(self):
        return self.title