from django.urls import re_path
from .views import *

My_app = 'Setting'

urlpatterns = [

    re_path(r'^list/token=(?P<token>[\w]+)/$', SettingList .as_view(), name='SettingList'),
    re_path(r'^change/setting/$', ChangeSetting.as_view(), name='ChangeSetting'),


]
