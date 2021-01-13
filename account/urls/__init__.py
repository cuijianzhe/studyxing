from account.urls import user
from account.urls import mod
from account.urls import permission
from account.urls import department

urlpatterns = user.urlpatterns + \
              mod.urlpatterns + \
              permission.urlpatterns + \
              department.urlpatterns
