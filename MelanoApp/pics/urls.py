from django.conf.urls import url
from . import views

app_name = 'pics'

urlpatterns = [
    #/pics/
    url(r'^$', views.IndexView.as_view(), name="index"),

    #/pics/<mark_id>/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(),name='detail'),

    #pics/mark/add/
    url(r'mark/add/$', views.MarkCreate.as_view(), name = "mark-add" ),

    #pics/mark/2/
    url(r'mark/^(?P<pk>[0-9]+)/$', views.MarkUpdate.as_view(), name = "mark-update" ),

    #pics/mark/2/delete
    url(r'mark/^(?P<pk>[0-9]+)/delete/$', views.MarkDelete.as_view(), name = "mark-delete" ),

    
]