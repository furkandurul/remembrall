from django.urls import path

from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('home', views.home, name='_home'),
	path('post/<int:post_id>/', views.post, name='post'),
	path('user_space', views.user_space, name='user_space'),
]
