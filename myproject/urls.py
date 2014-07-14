from django.conf.urls import patterns, include, url
from hello.views import LoginView, HomeView, TaskListView

urlpatterns = patterns('',
                       url(r'^login/$', LoginView.as_view()),
                       url(r'^lists/$', TaskListView.as_view()),
                       url(r'^$', HomeView.as_view()),
                       )
