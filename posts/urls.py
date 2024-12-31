from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
	path(
		route='<int:post_id>',
		view=views.ShowPost.as_view(),
		name='detail',
	),
	path(
		route='create/assignment/<int:channel_id>',
		view=views.CreateAssignmentPost.as_view(),
		name='create-assignment',
	),
	path(
		route='create/material/<int:channel_id>',
		view=views.CreateLearningMaterialPost.as_view(),
		name='create-material',
	),
	path(
		route='<int:pk>/update-assignment',
		view=views.UpdateAssignmentPost.as_view(),
		name='update-assignment',
	),
	path(
		route='<int:pk>/update-learning',
		view=views.UpdateLearningMaterialPost.as_view(),
		name='update-learning',
	),
	path(
		route='<int:pk>/delete',
		view=views.PostDeleteView.as_view(),
		name='delete',
	),
]
