from django.conf.urls import url
# from django.conf.urls.static import static
# from django.conf import settings
from . import views
                    
urlpatterns = [
    url(r'^$', views.med_dashboard),
    url(r'addchild$', views.addchild),
    url(r'child$', views.child),
    url(r'viewvaccine/(?P<dependent_id>\d+)$', views.viewvaccine),
    url(r'seevaccines/(?P<dependent_id>\d+)$', views.seevaccines),
    url(r'delete/(?P<dependent_id>\d+)$', views.delete),
    url(r'logout$', views.logout),
]

