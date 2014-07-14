from django.http import HttpResponse
from django.views.generic import View

class Home(View):
    def get(self, request):
        return HttpResponse('Hello World! Please try /login for some magic')

def login(request):
	from google.appengine.api import users
	user = users.get_current_user()

	if user:
		greeting = ('Welcome, %s! (<a href="%s">sign out</a>)' % (user.nickname(), users.create_logout_url('/')))
	
	else:
		greeting = ('<a href="%s">Sign in or register</a>.' % users.create_login_url('/'))
	
	return HttpResponse('<html><body>%s</body></html>' % greeting)