from django.conf.urls import url, include
from candle import views

urlpatterns = [
    url(r'^', include('django_alexa.urls')),
]
