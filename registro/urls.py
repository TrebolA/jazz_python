from django.conf.urls import url
from registro import views

urlpatterns = [
    url(r'^', views.home),
    url(r'^gracias/', views.thank_you, name="thank_you"),
]
