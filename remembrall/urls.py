from django.urls import path

from . import views

urlpatterns = [
	path("", views.home, name="root"),
	path("home", views.home, name="home"),
	path("post", views.post, name="post"),
	path("create_post", views.create_post, name="create_post"),
	path("post_list", views.post_list, name="post_list"),
]
