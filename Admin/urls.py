from django.urls import re_path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import *

My_app = 'Admin'

urlpatterns = [

    re_path('^operator/program/$', OperatorProgram.as_view(), name='OperatorProgram'),
    # re_path('^set/operator/program/$', set_operator_program.as_view(), name='SetOperatorProgram'),

]

urlpatterns = format_suffix_patterns(urlpatterns)
