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
from property.views import (home_view,
                            PropertyList,
                            property_sell,
                            PropertyDetail,
                            PropertyCreate,
                            PropertyDelete,
                            PropertyUpdate)

urlpatterns = [
    url(r'^$',home_view),
    url(r'^buy/',PropertyList.as_view(),name="buy"),
    url(r'^sell/',PropertyCreate.as_view(),name="sell"),
    url(r'^detail/(?P<pk>\d+)',PropertyDetail.as_view(),name="detail"),
    url(r'^delete/(?P<pk>\d+)',PropertyDelete.as_view(),name="delete"),
    url(r'^update/(?P<pk>\d+)',PropertyUpdate.as_view(),name="update"),
    # url(r'^create/(?P<pk>)',PropertyCreate.as_view(),name="create"),
]
