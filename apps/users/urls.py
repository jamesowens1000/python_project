from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^edit_user$', views.edit_user),
    url(r'^update$', views.update),
    url(r'^logout$', views.logout),
]