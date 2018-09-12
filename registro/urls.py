from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^gracias/$', views.gracias, name='gracias'),
    url(r'^csv/$', views.exportCsv),
]
