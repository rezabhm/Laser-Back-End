from django.urls import re_path
from .views import *

My_app = 'Admin'

urlpatterns = [

    re_path('^operator/program/$', operator_program.as_view(), name='OperatorProgram'),
    re_path('^set/operator/program/$', set_operator_program.as_view(), name='SetOperatorProgram'),

]
