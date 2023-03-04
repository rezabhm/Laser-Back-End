from django.urls import re_path
from .views import *

My_app = 'LazerApp'

urlpatterns = [

    re_path(r'^laser/area/list/$', LaserAreaList.as_view(), name='LaserAreaList'),
    re_path(r'^add/new/laser/area/$', AddNewLaserArea.as_view(), name='AddNewLaserArea'),
    re_path(r'^edit/laser/area/$', EditLaserArea.as_view(), name='EditLaserArea'),
    re_path(r'^delete/laser/area/$', DeleteLaserArea.as_view(), name='DeleteLaserArea'),

]
