from django import http

def home(request):
    return http.HttpResponse('Hello World! Please try /login for some magic')

def login(request):
	from google.appengine.api import users
	user = users.get_current_user()

	if user:
		greeting = ('Welcome, %s! (<a href="%s">sign out</a>)' % (user.nickname(), users.create_logout_url('/')))
	
	else:
		greeting = ('<a href="%s">Sign in or register</a>.' % users.create_login_url('/'))
	
	return http.HttpResponse('<html><body>%s</body></html>' % greeting)
