from django.db.models           import (
                                    ForeignKey, 
                                    CASCADE, 
                                    BooleanField,
                                    CharField
                                )
from django.utils.translation   import gettext_lazy as _
from .basemodel                 import BaseModel
from ..models                   import User


class Role(BaseModel):
    owner                           = ForeignKey(verbose_name = _("owner"), to = User, on_delete = CASCADE, related_name = 'role')
    title                           = CharField(_("title"), max_length = 40)
    create_role                     = BooleanField(_("create role"),                    default = False)
    list_role                       = BooleanField(_("list role"),                      default = False)
    retrieve_role                   = BooleanField(_("retrieve role"),                  default = False)
    update_role                     = BooleanField(_("update role"),                    default = False)
    destroy_role                    = BooleanField(_("destroy role"),                   default = False)
    create_account                  = BooleanField(_("create account"),                 default = False)
    list_account                    = BooleanField(_("list account"),                   default = False)
    retrieve_account                = BooleanField(_("retrieve account"),               default = False)
    update_account                  = BooleanField(_("update account"),                 default = False)
    destroy_account                 = BooleanField(_("destroy account"),                default = False)
    create_accountside_category     = BooleanField(_("create accountside_category"),    default = False)
    list_accountside_category       = BooleanField(_("list accountside_category"),      default = False)
    retrieve_accountside_category   = BooleanField(_("retrieve accountside_category"),  default = False)
    update_accountside_category     = BooleanField(_("update accountside_category"),    default = False)
    destroy_accountside_category    = BooleanField(_("destroy accountside_category"),   default = False)
    create_accountside              = BooleanField(_("create accountside"),             default = False)
    list_accountside                = BooleanField(_("list accountside"),               default = False)
    retrieve_accountside            = BooleanField(_("retrieve accountside"),           default = False)
    update_accountside              = BooleanField(_("update accountside"),             default = False)
    destroy_accountside             = BooleanField(_("destroy accountside"),            default = False)
    create_expense                  = BooleanField(_("create expense"),                 default = False)
    list_expense                    = BooleanField(_("list expense"),                   default = False)
    retrieve_expense                = BooleanField(_("retrieve expense"),               default = False)
    update_expense                  = BooleanField(_("update expense"),                 default = False)
    destroy_expense                 = BooleanField(_("destroy expense"),                default = False)
    create_note                     = BooleanField(_("create note"),                    default = False)
    list_note                       = BooleanField(_("list note"),                      default = False)
    retrieve_note                   = BooleanField(_("retrieve note"),                  default = False)
    update_note                     = BooleanField(_("update note"),                    default = False)
    destroy_note                    = BooleanField(_("destroy note"),                   default = False)
    create_subject_category         = BooleanField(_("create subject_category"),        default = False)
    list_subject_category           = BooleanField(_("list subject_category"),          default = False)
    retrieve_subject_category       = BooleanField(_("retrieve subject_category"),      default = False)
    update_subject_category         = BooleanField(_("update subject_category"),        default = False)
    destroy_subject_category        = BooleanField(_("destroy subject_category"),       default = False)
    create_subject                  = BooleanField(_("create subject"),                 default = False)
    list_subject                    = BooleanField(_("list subject"),                   default = False)
    retrieve_subject                = BooleanField(_("retrieve subject"),               default = False)
    update_subject                  = BooleanField(_("update subject"),                 default = False)
    destroy_subject                 = BooleanField(_("destroy subject"),                default = False)
    create_workspace                = BooleanField(_("create workspace"),               default = False)
    list_workspace                  = BooleanField(_("list workspace"),                 default = False)
    retrieve_workspace              = BooleanField(_("retrieve workspace"),             default = False)
    update_workspace                = BooleanField(_("update workspace"),               default = False)
    destroy_workspace               = BooleanField(_("destroy workspace"),              default = False)