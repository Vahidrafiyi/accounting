from django.db.models           import (TextField, ForeignKey, CASCADE, FloatField)
from django.utils.translation   import gettext_lazy as _

from .basemodel                 import BaseModel
from core.models                import User
from .accountside               import AccountSide


class WorkSpace(BaseModel):
    owner           = ForeignKey(verbose_name = _("owner"), to = User, related_name = "workspace_user", on_delete = CASCADE)                                
    accountside     = ForeignKey(verbose_name = _("accountside"), to = AccountSide, related_name = "workspace_tarafhesab", on_delete = CASCADE)                                
    description     = TextField(_("description"), max_length = 1000, null = True, blank=True) 
    received_money  = FloatField(_("received money"),   default = 0, null = True, blank = True)
    paid_money      = FloatField(_("paid money"),       default = 0, null = True, blank = True)
    balance         = FloatField(_("balance"),          default = 0, null = True, blank = True)

    class Meta:
        ordering = ['-accountside']

    def __str__(self):
        return self.accountside.name