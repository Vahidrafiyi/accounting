from django.urls                                        import path, include

from rest_framework_nested.routers                      import DefaultRouter, NestedDefaultRouter


from .views.auth_token.auth_token                       import AuthTokenViewSet
from .views.account.account                             import AccountViewset
from .views.accountside.accountside                     import AccountSideViewset
from .views.accountside_category.accountside_category   import AccountSideCategoryViewset
from .views.expense.expense                             import ExpenseViewset
from .views.note.note                                   import NoteViewset
from .views.subject.subject                             import SubjectViewset
from .views.subject_category.subject_category           import SubjectCategoryViewset
from .views.user.user                                   import UserViewSet
from .views.workspace.workspace                         import WorkSpaceViewset

router = DefaultRouter()
router.register('tokens',                   AuthTokenViewSet)
router.register('users',                    UserViewSet)
router.register('accountside-categories',   AccountSideCategoryViewset)
router.register('expenses',                 ExpenseViewset)
router.register('notes',                    NoteViewset)
router.register('subject-categories',       SubjectCategoryViewset)

user_router                 = NestedDefaultRouter(router, 'users', lookup = 'users')
user_router.register('accounts', AccountViewset, basename = 'account')
user_router.register('workspaces', WorkSpaceViewset, basename = 'workspace')

accountside_category_router = NestedDefaultRouter(router, 'accountside-categories', lookup = 'accountside_categories')
accountside_category_router.register('accountsides', AccountSideViewset, basename = 'accountside-category')

subject_category_router     = NestedDefaultRouter(router, 'subject-categories', lookup = 'subject_categories')
subject_category_router.register('subjects', SubjectViewset, basename = 'subject')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(user_router.urls)),
    path('', include(accountside_category_router.urls)),
    path('', include(subject_category_router.urls)),
]