from django.db.models           import (CharField, TextField, DateTimeField,
                                        ForeignKey, CASCADE, BooleanField, FloatField)
from django.utils.translation   import gettext_lazy as _

from .basemodel                 import BaseModel
from core.models                import User
from .accountside_category      import AccountSideCategory


class AccountSide(BaseModel):                                 
    owner               = ForeignKey(verbose_name = _("owner"), to = User, related_name = "accountside_user", on_delete = CASCADE)
    category            = ForeignKey(verbose_name = _("category"), to = AccountSideCategory, related_name = "accountsides", on_delete = CASCADE)
    name                = CharField(_("name"), max_length = 200, null = True, blank = True)
    phone               = CharField(_("phone"), max_length = 12, null = True, blank = True)
    is_natural_person   = BooleanField(_("natural person?"), help_text = "طرف حساب شخصی حقیقی است؟", default = True)
    description         = TextField(_("description"), max_length = 1000, null = True, blank=True)
    received_money      = FloatField(_("received money"), default = 0, null = True, blank = True)
    paid_money          = FloatField(_("paid money"), default = 0, null = True, blank = True)
    balance             = FloatField(_("balance"), help_text = "باقی مانده", default = 0, null = True, blank = True)

    class Meta:
        ordering = ['-name']

    def __str__(self):
        return self.name