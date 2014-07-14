from django.conf.urls import patterns, include, url
from hello.views import Home
from hello.views import TaskList
urlpatterns = patterns('',
                       url(r'^login/$', 'hello.views.login'),
                       url(r'^lists/$', TaskList.as_view()),
                       url(r'^$', Home.as_view()),
                       )
