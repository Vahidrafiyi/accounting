from django.contrib                 import admin

from .modelsf.account               import Account
from .modelsf.accountside_category  import AccountSideCategory
from .modelsf.accountside           import AccountSide
from .modelsf.expense               import Expense
from .modelsf.note                  import Note
from .modelsf.subject_category      import SubjectCategory
from .modelsf.subject               import Subject
from .modelsf.workspace             import WorkSpace
from .models                        import User
from .modelsf.role                  import Role


class RoleAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
    )


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'username',
        'phone',
        'first_name',
        'last_name',
        'date_joined'
    )


class AccountAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'owner',
        'account_title',
        'bank_name',
        'account_number',
        'card_number',
        'shaba_number',
        'received_money',
        'paid_money',
        'balance',
    )


class AccountSideCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'owner',
        'title',
        'description'
    )


class AccountSideAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'owner',
        'category',
        'name',
        'phone',
        'is_natural_person',
        'received_money',
        'paid_money',
        'balance',
    )


class ExpenseAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'owner',
        'account',
        'accountside',
        'subject',
        'workspace',
        'date_time',
        'title',
        'price',
        'is_received_money',
        'description'
    )


class NoteAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'owner',
        'title'
    )


class SubjectCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'owner',
        'title'
    )


class SubjectAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'owner',
        'category',
        'title',
    )


class WorkSpaceAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'accountside',
        'received_money',
        'paid_money',
        'balance',
    )


admin.site.register(User,                   UserAdmin)
admin.site.register(Role,                   RoleAdmin)
admin.site.register(Account,                AccountAdmin)
admin.site.register(AccountSideCategory,    AccountSideCategoryAdmin)
admin.site.register(AccountSide,            AccountSideAdmin)
admin.site.register(Expense,                ExpenseAdmin)
admin.site.register(Note,                   NoteAdmin)
admin.site.register(SubjectCategory,        SubjectCategoryAdmin)
admin.site.register(Subject,                SubjectAdmin)
admin.site.register(WorkSpace,              WorkSpaceAdmin)