from django.urls import re_path
from .views import *

My_app = 'Core'

urlpatterns = [

    re_path(r'^signup/customer/$', SignUpCustomer.as_view(), name='SignUpCustomer'),
    re_path(r'^signup/admin/$', SignUpAdmin.as_view(), name='SignUpAdmin'),
    re_path(r'^login/$', Login.as_view(), name='Login'),
    re_path(r'^logout/token=(?P<token>[\w]+)/$', LogOut.as_view(), name='LogOut'),
    re_path(r'^forgot/password/$', ForgotPassword.as_view(), name='ForgotPassword'),
    re_path(r'^prove/forgot/password/$', ProveForgotPassword.as_view(), name='ProveForgotPassword'),
    re_path(r'^change/password/$', ChangePassword.as_view(), name='ChangePassword'),
    re_path(r'^user/list/token=(?P<token>[\w]+)/$', UserList.as_view(), name='UserList'),
    re_path(r'^operator/list/token=(?P<token>[\w]+)/$', OperatorList.as_view(), name='OperatorList'),
    re_path(r'^customer/list/token=(?P<token>[\w]+)/$', CustomerList.as_view(), name='CustomerList'),
    re_path(r'^comment/list/token=(?P<token>[\w]+)/$', CommentList.as_view(), name='CommentList'),
    re_path(r'^customer/add/to/charge/$', CustomerAdd2Charge.as_view(), name='CustomerAdd2Charge'),
    re_path(r'^delete/user/$', DeleteUser.as_view(), name='DeleteUser'),
    re_path(r'^customer/information/$', CustomerInf.as_view(), name='CustomerInf'),
    re_path(r'^change/user/information/$', ChangeUserInformation.as_view(), name='ChangeUserInf'),
    re_path(r'^enter/exit/operator/$', EnterExitOperator.as_view(), name='EnterExitOperator'),

]
