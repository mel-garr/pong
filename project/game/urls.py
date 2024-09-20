from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('home/', home, name='home'),
    path('auth-status/', check_login_status, name='auth_status'),
    path('login/', login, name='loginO'),
    path('lobby/', lobby, name='lobby'),
    path('offmulti/', offmulti, name='offmulti'),
    path('onmulti/', onmulti, name='onmulti'),


    path('creat_new_room/', creat_new_room, name='creat_new_room'),
    # path('lobby2/', lobby2, name='lobby2'),
    # path('room/<str:room_name>', room_detail, name='room_detail')

    # path('login3/', login3, name='login3'),
]