"""realML URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from property.views import home_view,about_view,contact_view,property_list,property_sell
from django.conf.urls import include


urlpatterns = [
    url(r'^$',home_view),
    url(r'^admin/', admin.site.urls),
    url(r'^home/',home_view,name="home"),
    url(r'^contact/',contact_view,name="contact"),
    url(r'^about/',about_view,name='about'),
    url(r'^property/',include("property.urls",namespace="property")),
]

