from django.shortcuts import render
from django.shortcuts import get_object_or_404, render, render_to_response 
from django.views.decorators.http import require_POST, require_GET
from django.contrib.auth import authenticate, login, logout
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.template import RequestContext

# Create your views here.
def index(request):
	return render_to_response('index.html', {}, context_instance=RequestContext(request))

def login(request):
	return render_to_response('login.html', {}, context_instance=RequestContext(request))

"""
Form post views. Django view method
"""
def attempt_login(request):
	try:
		username = request.POST['username']
		password = request.POST['password']
	except(KeyError):
		raise Http404

	user = authenticate(username=username,password=password)
	
	if user is not None:		
		login(request, user)		
		return HttpResponseRedirect('/')
	else:
		return HttpResponseRedirect('/Login/')