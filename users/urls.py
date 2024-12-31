from django.contrib.auth.views import (
	LogoutView,
	PasswordChangeDoneView,
	PasswordChangeView,
)
from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
	path(
		route='login/',
		view=views.LoginUser.as_view(),
		name='login',
	),
	path(
		route='logout/',
		view=LogoutView.as_view(),
		name='logout',
	),
	path(
		route='register/',
		view=views.RegisterUser.as_view(),
		name='register',
	),
	path(
		route='<int:pk>',
		view=views.UserDetailView.as_view(),
		name='detail',
	),
	path(
		route='password-change',
		view=views.CustomPasswordChangeView.as_view(),
		name='password-change',
	),
	path(
		route='password-change-done',
		view=views.CustomPasswordChangeDoneView.as_view(),
		name='password-change-done',
	),
	path(
		route='<int:pk>/update',
		view=views.UserUpdateView.as_view(),
		name='update',
	),
]
