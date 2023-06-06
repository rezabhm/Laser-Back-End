from django.urls import re_path
from .views import *

My_app = 'Payment'

urlpatterns = [

    re_path(r'^off/code/list/$', OffCodeList.as_view(), name='OffCodeList'),
    re_path(r'^off/code/delete/$', OffCodeDelete.as_view(), name='OffCodeDelete'),
    re_path(r'^off/code/$', OffCode.as_view(), name='OffCode'),
    re_path(r'^off/code/create/$', OffCodeCreate.as_view(), name='OffCodeCreate'),
    re_path(r'^off/code/add/reserve/$', OffCodeAddReserve.as_view(), name='OffCodeAddReserve'),
    re_path(r'^multiple/payment/$', MultiplePayment.as_view(), name='MultiplePayment'),

]
