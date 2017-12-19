from django.conf.urls import url
from .views import (
    post_create,
    post_delete,
    post_list,
    post_update,
    post_detail,

)




urlpatterns = [
    url(r'^create/$', post_create),
    url(r'^$', post_list, name='list'),
    url(r'^(?P<id>\d+)/edit/$', post_update, name='update'),
    url(r'^(?P<id>\d+)/delete/$', post_delete),
    url(r'^(?P<id>\d+)/$', post_detail, name='detail'),


]
