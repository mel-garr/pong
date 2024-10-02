from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('home/', home, name='home'),
    path('auth-status/', check_login_status, name='auth_status'),
    path('login/', login, name='loginO'),
    path('lobby/', lobby, name='lobby'),
    path('setuplobbyoff/', setuplobbyoff, name='setuplobbyoff'),
    path('<int:room_id>/', offmulti_view, name='offmulti'),
]

    # path('login3/', login3, name='login3'),
    # path('offmulti/', offmulti, name='offmulti'),