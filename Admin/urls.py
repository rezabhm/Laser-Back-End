from django.urls import re_path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import *

My_app = 'Admin'

urlpatterns = [

    re_path(r'^operator/program/list/(?P<date_year>[\d]+)/(?P<date_month>[\d]+)/(?P<date_day>[\d]+)/$', OperatorProgramList.as_view(), name='OperatorProgramList'),
    re_path(r'^set/operator/program/$', SetOperatorProgram.as_view(), name='SetOperatorProgram'),
    re_path(r'^week/time/(?P<week>[-+]?\d+)/$', WeekTime.as_view(), name='WeekTime'),

]

urlpatterns = format_suffix_patterns(urlpatterns)
