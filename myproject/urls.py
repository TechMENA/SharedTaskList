from django.conf.urls import patterns, include, url
from hello.views import Home
urlpatterns = patterns('',
    url(r'^$', Home.as_view()),
)
