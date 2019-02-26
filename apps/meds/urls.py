from django.conf.urls import url
# from django.conf.urls.static import static
# from django.conf import settings
from . import views
                    
urlpatterns = [
    url(r'^$', views.med_dashboard),
    url(r'child$', views.child),
    url(r'addchild$', views.addchild),
    url(r'^vaccines$', views.vaccines),
    url(r'^seevaccines$', views.seevaccines),
    url(r'logout$', views.logout),
]