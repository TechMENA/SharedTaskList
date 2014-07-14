from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'hello.views.home'),
    url(r'^login/$', 'hello.views.login'),
)
