from django.urls import re_path
from .views import *

My_app = 'Reception'

urlpatterns = [

    re_path(r'^operator/token=(?P<token>[\w]+)/$', Operator.as_view(), name='Operator'),

]
