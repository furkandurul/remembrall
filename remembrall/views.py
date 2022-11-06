from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


from .models import User, Post


def landing_page(request):
	template = loader.get_template("landing_page.html")
	context = {}
	return HttpResponse(template.render(context, request))

def home(request):
	template = loader.get_template("home.html")
	context = {}
	return HttpResponse(template.render(context, request))

def post_list(request):
	template = loader.get_template("remembrall/post_list.html")
	context = {}
	return HttpResponse(template.render(context, request))

def post(request):
	template = loader.get_template("remembrall/post.html")
	context = {}
	return HttpResponse(template.render(context, request))
