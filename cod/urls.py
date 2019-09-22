from django.conf.urls import url
from django.views.generic import RedirectView
from . import views

urlpatterns = [
        url(r'^$', RedirectView.as_view(url='/new/', permanent=True)),
        url(r'^(?P<pk>[0-9]+)/$', views.detail, name='detail'),
        ]
