from django.db.models           import (TextField, ForeignKey, CASCADE, DateField, CharField)
from django.utils.translation   import gettext_lazy as _

from .basemodel                 import BaseModel
from .user                      import User


class Note(BaseModel):
    owner       = ForeignKey(verbose_name = _("owner"), to = User, related_name = "user_notes", on_delete = CASCADE)
    title       = CharField(_("title"),         max_length = 400,   null = True, blank = True)  
    description = TextField(_("description"),   max_length = 10000, null = True, blank = True) 

    class Meta:
        ordering = ['-title']

    def __str__(self):
        return self.title