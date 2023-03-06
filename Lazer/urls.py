"""

Lazer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/

Examples:

Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')

Class-based views

    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')

Including another URLconf

    1. Import to include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

"""

from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Laser API')

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', schema_view),
    path('Admin/', include('Admin.urls')),
    path('Core/', include('Core.urls')),
    path('Laser/', include('LazerApp.urls')),
    path('Payment/', include('Payment.urls')),
    path('Reception/', include('Reception.urls')),
    path('Reserve/', include('Reserve.urls')),
    path('Setting/', include('Setting.urls')),
    path('zarin/pall/', include('ZarinPall.urls')),

]
