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
                            about_view,
                            AboutView,
                            contact_view,
                            property_list,
                            property_sell,)


from django.conf.urls import include
from django.conf.urls.static import static
from django.views.static import serve
from django.conf import settings
from profiles.views import (LoginView,
                            logout_view,
                            registration,
                            profile_update_view,
                            profile_view)
urlpatterns = [
    url(r'^$',home_view),
    url(r'^admin/', admin.site.urls),
    url(r'^home/',home_view,name="home"),
    url(r'^contact/',contact_view,name="contact"),
    url(r'^about/',AboutView.as_view(),name='about'),
    url(r'^property/',include("property.urls",namespace="property")),
    url(r'^login/',LoginView,name="login"),
    url(r'^logout/',logout_view,name="logout"),
    url(r'^registration/',registration,name="signup"),
    url(r'^profile/update/',profile_update_view,name="p-update"),
    url(r'^profile/',profile_view,name="profile"),
    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)