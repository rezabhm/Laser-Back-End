from django.urls import re_path
from .views import *

My_app = 'Reserve'

urlpatterns = [

    re_path(r'^reserve/list/$', ReserveList .as_view(), name='ReserveList'),
    re_path(r'^user/reserve/list/$', UserReserveList .as_view(), name='UserReserveList'),
    re_path(r'^reserve/information/$', ReserveInformation.as_view(), name='ReserveInformation'),
    re_path(r'^cancel/reserve/$', CancelReserve.as_view(), name='CancelReserve'),
    re_path(r'^cancel/time/range/$', CancelTimeRange.as_view(), name='CancelTimeRange'),
    re_path(r'^reserve/laser/area/$', ReserveLaserArea.as_view(), name='ReserveLaserArea'),
    re_path(r'^edit/reserve/laser/area/$', EditReserveLaserArea.as_view(), name='EditReserveLaserArea'),
    re_path(r'^reception/add/reserve/$', ReceptionAddReserve.as_view(), name='ReceptionAddReserve'),
    re_path(r'^prove/reserve/$', ProveReserve.as_view(), name='ProveReserve'),
    re_path(r'^time/list/(?P<reserve_id>[\w]+)/$', TimeList.as_view(), name='TimeList'),
    re_path(r'^reserve/time/range/(?P<reserve_id>[\w]+)/$', ReserveTimeRange.as_view(), name='ReserveTimeRange'),
    re_path(r'^cancel/time/range/(?P<reserve_id>[\w]+)/$', CancelReserveTimeRange.as_view(), name='CancelReserveTimeRange'),
    re_path(r'^client/pending/reserve/$', ClientPendingReserve.as_view(), name='ClientPendingReserve'),
    re_path(r'^client/add/time/$', ClientAddTimeReserve.as_view(), name='ClientAddTimeReserve'),
    re_path(r'^time/range/list/$', TimeRangeList.as_view(), name='TimeRangeList'),

]
