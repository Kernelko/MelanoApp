from django.conf.urls import url
from . import views

app_name = 'pics'

urlpatterns = [
    #/pics/
    url(r'^$', views.index, name="index"),

    #/pics/<mark_id>/
    url(r'^(?P<mark_id>[0-9]+)/$', views.detail,name='detail'),

    #/pics/<mark_id>/cancerous
    url(r'^(?P<mark_id>[0-9]+)/cancerous/$', views.cancerous,name='cancerous')
]