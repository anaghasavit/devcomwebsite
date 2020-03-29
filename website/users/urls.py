from django.conf.urls import url
from .import views

app_name='users'

urlpatterns=[
    url(r'^signin/$',views.userform,name="signin"),
    url(r'^login/$',views.loginform,name="login"),
    url(r'^logout/$',views.logoutform,name="logout"),
]