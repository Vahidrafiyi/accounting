from django.db.models           import (ForeignKey, CASCADE, CharField, TextField,
                                        DateTimeField, IntegerField, ImageField, BooleanField)
from django.utils.translation   import gettext_lazy as _

from .basemodel                 import BaseModel
from .user                      import User
from .subject                   import Subject
from .accountside               import AccountSide
from .workspace                 import WorkSpace
from .account                   import Accout


class Expense(BaseModel):
    owner               = ForeignKey(verbose_name = _("owner"),         to = User,          related_name = 'user_expenses',         on_delete = CASCADE)
    account             = ForeignKey(verbose_name = _("account"),       to = Accout,        related_name = 'account_expenses',      on_delete = CASCADE, null = True, blank = True)
    accountside         = ForeignKey(verbose_name = _("accountside"),   to = AccountSide,   related_name = 'accountside_expenses',  on_delete = CASCADE)
    subject             = ForeignKey(verbose_name = _("subject"),       to = Subject,       related_name = 'subject_expenses',      on_delete = CASCADE, null = True, blank = True)
    workspace           = ForeignKey(verbose_name = _("workspace"),     to = WorkSpace,     related_name = 'workspace_expenses',    on_delete = CASCADE, null = True, blank = True)
    date_time           = DateTimeField(_("date time"))
    title               = CharField(_("title"), max_length = 200)
    price               = IntegerField(_("price"), )
    image               = ImageField(verbose_name = _("image"), upload_to = 'factors/', null = True, blank = True)
    is_received_money   = BooleanField(_("is received money"), default = False)
    description         = TextField(_("description"), max_length = 1000, blank = True)

    class Meta:
        ordering = ['-date_time']

    def __str__(self):
        return self.title