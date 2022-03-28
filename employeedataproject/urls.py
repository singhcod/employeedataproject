"""employeedataproject URL Configuration

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
from employeedata import views 

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^data/',views.employeedata_view),
    #url(r'^$',views.fetching_dat),
    url(r'^$',views.home_page, name='home_page'),
    url(r'^hyd_data/',views.hyderabad_data, name='hyd_data'),
    url(r'^bang_data/',views.bangalore_data, name='bang_data'),
    url(r'^chennai_data/',views.chennai_data, name='chennai_data'),
    url(r'^pune_data/',views.pune_data, name='pune_data'),
    url(r'^delhi_data/',views.delhi_data, name='delhi_data'),

    url(r'^register/',views.register_view, name='register'),
    url(r'^login/',views.login_view, name='login'),
    url(r'^logout',views.logout_view, name='logout'),
]
