from django.urls import re_path
from . import views

urlpatterns = [
    # /music/
    re_path(r'^$', views.index, name='index'),
    # /music/id:1
    re_path(r'^(?P<Muscician_id>[0-9]+)/$', views.detail, name='detail')
]
