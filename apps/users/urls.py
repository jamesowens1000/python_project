from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^dashboard$', views.dashboard),
    url(r'^edit_page$', views.edit_page),
    url(r'^users/update$', views.update),
    url(r'^logout$', views.logout),
]