from django.urls import path

from . import views

app_name = 'tests_tests'

urlpatterns = [
	path(
		route='create',
		view=views.TestCreateView.as_view(),
		name='create',
	),
]
