from django.conf.urls import url
from login.views import *


urlpatterns = [
    url(r'^index/$', index),
    url(r'^register/$', register),
    url(r'^login/$', login),
    url(r'^confirm/$', user_confirm),
    url(r'^logout/$',logout),
    url(r'^', index),

]