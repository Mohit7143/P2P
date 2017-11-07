from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^ack/$',views.ack,name="ack"),
    url(r'^get/$',views.get_list,name="get"),
    url(r'^find/$',views.find,name="find"),
    url(r'^up/$',views.download,name="up"),
]
