from django.conf.urls import patterns, include, url
from hello.views import Home
urlpatterns = patterns('',
    url(r'^login/$', 'hello.views.login'),
    url(r'^$', Home.as_view()),
)
