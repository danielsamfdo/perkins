from django.conf.urls import url, include
from candle import views

urlpatterns = [
    url(r'^plugin', views.plugin),
    url(r'^test/form', views.render_test_html_form),
    url(r'^', include('django_alexa.urls')),

]
