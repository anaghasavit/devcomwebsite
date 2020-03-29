from django.conf.urls import url
from .import views

urlpatterns=[
    url(r'^$', views.homepage, name="homepage"),
    url(r'^newpost/$',views.newpost,name="newpost"),
    url(r'^(?P<slug>[\w-]+)/$',views.postdetails,name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', views.editpost, name='editpost'),
]
 