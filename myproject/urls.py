from django.conf.urls import patterns, include, url
from hello.views import HomeView, TaskListView

urlpatterns = patterns('',
                       url(r'^login/$', 'hello.views.LoginView'),
                       url(r'^lists/$', TaskListView.as_view()),
                       url(r'^$', HomeView.as_view()),
                       )
