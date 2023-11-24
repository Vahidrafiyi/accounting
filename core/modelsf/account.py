from django.db.models           import (TextField, ForeignKey, CASCADE,
                                        CharField, PositiveIntegerField)
from django.utils.translation   import gettext_lazy as _

from .basemodel                 import BaseModel
from core.models                import User


class Account(BaseModel):
    owner           = ForeignKey(verbose_name = _("owner"), to = User, on_delete = CASCADE)
    account_title   = CharField(_("account title"),     max_length = 200, unique = True)
    bank_name       = CharField(_("bank name"),         max_length = 200)
    account_number  = CharField(_("account number"),    max_length = 50, blank = True)
    card_number     = CharField(_("card number"),       max_length = 50, blank = True)
    shaba_number    = CharField(_("shaba number"),      max_length = 50, blank = True)
    description     = TextField(_("description"),       max_length = 1000, null = True, blank = True)
    received_money  = PositiveIntegerField(_("received money"),   default = 0, null = True, blank = True)
    paid_money      = PositiveIntegerField(_("paid money"),       default = 0, null = True, blank = True)
    balance         = PositiveIntegerField(_("balance"),          default = 0, null = True, blank = True)

    class Meta:
        ordering = ['-account_title']

    def __str__(self):
        return self.account_title