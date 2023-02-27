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


from rest_framework import response, schemas
from rest_framework.decorators import api_view, renderer_classes
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer


class CustomRenderer(OpenAPIRenderer):
    def get_customizations(self):
        data = super().get_customizations()
        data['host'] = 'backend.lianalaser.com/'
        return data


@api_view()
@renderer_classes([SwaggerUIRenderer, CustomRenderer])
def swagger_view(request):
    generator = schemas.SchemaGenerator(title='Your title')
    return response.Response(generator.get_schema(request=request))


schema_view = get_swagger_view(title='Laser API')

urlpatterns = [

    path('admin/', admin.site.urls),
    path('swagger/', schema_view),
    path('docs/', swagger_view),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('Admin/', include('Admin.urls')),
    path('Core/', include('Core.urls')),
    path('Laser/', include('LazerApp.urls')),
    path('Payment/', include('Payment.urls')),
    path('Reception/', include('Reception.urls')),
    path('Reserve/', include('Reserve.urls')),
    path('Setting/', include('Setting.urls')),

]
