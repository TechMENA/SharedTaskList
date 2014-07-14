from django.http import HttpResponse
from django.views.generic import View

from google.appengine.api import users

from .models import TaskList

class HomeView(View):
    def get(self, request):
        return HttpResponse('Hello World! Please try /login for some magic')


def LoginView(request):
    user = users.get_current_user()

    if user:
        greeting = ('Welcome, %s! (<a href="%s">sign out</a>)' %
                    (user.nickname(), users.create_logout_url('/')))

    else:
        greeting = ('<a href="%s">Sign in or register</a>.' % users.create_login_url('/'))

    return HttpResponse('<html><body>%s</body></html>' % greeting)


class TaskListView(View):
    def get(self, request):
        return HttpResponse('Hello TaskList!')

    def post(self, request):
        return HttpResponse('post TaskList!')

    def put(self, request):
        return HttpResponse('put TaskList!')

    def delete(self, request):
        return HttpResponse('delete TaskList!')

