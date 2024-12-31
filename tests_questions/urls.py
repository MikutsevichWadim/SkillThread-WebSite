from django.urls import path

from . import views

app_name = 'channels'

urlpatterns = [
	path(
		route='create',
		view=views.TestCreateView.as_view(),
		name='create',
	),
]
