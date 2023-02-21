from django.urls import re_path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import *

My_app = 'Admin'

urlpatterns = [

    re_path('^operator/program/list/$', OperatorProgramList.as_view(), name='OperatorProgramList'),
    re_path('^set/operator/program/$', SetOperatorProgram.as_view(), name='SetOperatorProgram'),

]

urlpatterns = format_suffix_patterns(urlpatterns)
