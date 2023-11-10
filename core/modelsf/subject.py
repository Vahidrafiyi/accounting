from django.db.models           import (ForeignKey, CASCADE, CharField, TextField)
from django.utils.translation   import gettext_lazy as _

from .basemodel                 import BaseModel
from core.models                import User
from .subject_category          import SubjectCategory



class Subject(BaseModel):                            
    owner       = ForeignKey(verbose_name = _("owner"),     to = User, related_name = "user_topics", on_delete = CASCADE)                                
    category    = ForeignKey(verbose_name = _("category"),  to = SubjectCategory, related_name = "category_topics", on_delete = CASCADE)                                
    title       = CharField(_("title"),         max_length = 200,   null = True, blank = True)  
    description = TextField(_("description"),   max_length = 1000,  null = True, blank = True) 

    class Meta:
        ordering = ['-title']

    def __str__(self):
        return self.title