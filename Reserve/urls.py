from django.urls import re_path
from .views import *

My_app = 'Reserve'

urlpatterns = [

    re_path(r'^reserve/list/$', ReserveList .as_view(), name='ReserveList'),
    re_path(r'^user/reserve/list/$', UserReserveList .as_view(), name='UserReserveList'),
    re_path(r'^reserve/information/$', ReserveInformation.as_view(), name='ReserveInformation'),
    re_path(r'^cancel/reserve/$', CancelReserve.as_view(), name='CancelReserve'),
    re_path(r'^reserve/laser/area/$', ReserveLaserArea.as_view(), name='ReserveLaserArea'),
    re_path(r'^edit/reserve/laser/area/$', EditReserveLaserArea.as_view(), name='EditReserveLaserArea'),
    re_path(r'^reception/add/reserve/$', ReceptionAddReserve.as_view(), name='ReceptionAddReserve'),

]
