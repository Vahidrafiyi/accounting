import os

from django.db.models           import (CharField, TextField, ImageField, ForeignKey, CASCADE)
from django.contrib.auth.models import AbstractUser
from django.core.validators     import RegexValidator
from django.utils.translation   import gettext_lazy as _

from .modelsf.basemodel         import BaseModel
from .modelsf.role              import Role
from .managers                  import UserManager

def user_image_directory(instance, filename):
    # ext      = filename.split('.')[-1]                  # Seprate the file ext.
    # filename = "%s_1.%s" % ("instance.user.id", ext)    # rename the file with user id
    # directory = FileUpload.owner.id
    return os.path.join(filename)


# for user manager
class User(BaseModel, AbstractUser):
    phone           = CharField(_("phone"), max_length = 17, blank = False, unique = True)
    address         = TextField(_("address"), max_length = 1000, blank = True, null = True) 
    image           = ImageField(_("image"), upload_to = user_image_directory, null = True, blank = True)
    role            = ForeignKey(verbose_name = _("permissions"), to = Role, on_delete = CASCADE, related_name = 'users')
    objects         = UserManager()
    REQUIRED_FIELDS = ['email', 'phone']