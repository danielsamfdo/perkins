from django.conf.urls import url, include
from candle import views

urlpatterns = [
    url(r'^$', views.main),
    url(r'^alexa', views.alexa),
]
