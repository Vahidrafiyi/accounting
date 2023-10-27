from django.db.models           import (TextField, ForeignKey, CASCADE, FloatField,
                                        CharField, IntegerField)
from django.utils.translation   import gettext_lazy as _

from .basemodel                 import BaseModel
from .user                      import User


class Accout(BaseModel):
    owner           = ForeignKey(verbose_name = _("owner"), to = User, on_delete = CASCADE)
    account_title   = CharField(_("account title"),     max_length = 200)
    bank_name       = CharField(_("bank name"),         max_length = 200)
    account_number  = TextField(_("account number"),    max_length = 50, blank = True)
    card_number     = TextField(_("card number"),       max_length = 50, blank = True)
    shaba_number    = TextField(_("shaba number"),      max_length = 50, blank = True)
    mojoudi         = IntegerField(_("mojoudi"), default = 0)
    description     = TextField(_("description"),       max_length = 1000, null = True, blank = True)
    received_money  = FloatField(_("received money"),   default = 0, null = True, blank = True)
    paid_money      = FloatField(_("paid money"),       default = 0, null = True, blank = True)
    balance         = FloatField(_("balance"),          default = 0, null = True, blank = True)

    class Meta:
        ordering = ['-hesab_name']

    def __str__(self):
        return self.hesab_name