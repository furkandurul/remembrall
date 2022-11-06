from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


from .models import User, Post

def home(request):
	template = loader.get_template("home.html")
	context = {}
	return HttpResponse(template.render(context, request))

"""
def login(request):
	template = loader.get_template("registration/login.html")
	context = {}
	return HttpResponse(template.render(context, request))
"""

def post(request, post_id):
	template = loader.get_template("remembrall/post.html")
	context = {}
	return HttpResponse(template.render(context, request))

def user_space(request):
	#user_post_list = Post.objects.filter(creator_id=user_id)
	template = loader.get_template("remembrall/user_space.html")
	context = {}
	return HttpResponse(template.render(context, request))
