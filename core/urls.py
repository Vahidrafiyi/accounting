from django.urls                                        import path, include

from rest_framework_nested.routers                      import DefaultRouter, NestedDefaultRouter

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
router.register('users',                UserViewSet)
router.register('accounts',             AccountViewset)
router.register('accountsides',         AccountSideViewset)
router.register('expenses',             ExpenseViewset)
router.register('notes',                NoteViewset)
router.register('subjects',             SubjectViewset)
router.register('subject-categories',   SubjectCategoryViewset)
router.register('workspaces',           WorkSpaceViewset)

accountside_router = NestedDefaultRouter(router, 'accountsides', lookup = 'accountsides')
accountside_router.register('accountside-categories', AccountSideCategoryViewset, basename = 'accountside-category')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(accountside_router.urls))
]