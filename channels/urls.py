from django.urls import path

from . import views

app_name = 'channels'

urlpatterns = [
	path(
		route='',
		view=views.SearchChannels.as_view(),
		name='search',
	),
	path(
		route='create',
		view=views.CreateChannel.as_view(),
		name='create',
	),
	path(
		route='of-user',
		view=views.UserChannels.as_view(),
		name='of-user',
	),
	path(
		route='<int:pk>',
		view=views.ChannelDetail.as_view(),
		name='detail',
	),
	path(
		route='<int:channel_id>/posts',
		view=views.ChannelPosts.as_view(),
		name='post-list',
	),
	path(
		route='<int:channel_id>/quizes',
		view=views.ChannelQuizes.as_view(),
		name='quizes',
	),
	path(
		route='<int:channel_id>/questions',
		view=views.ChannelQuestions.as_view(),
		name='questions',
	),
	path(
		route='<int:channel_id>/update',
		view=views.UpdateChannel.as_view(),
		name='update',
	),
	path(
		route='<int:channel_id>/subscribe',
		view=views.Subscribe.as_view(),
		name='subscribe',
	),
	path(
		route='<int:channel_id>/unsubscribe',
		view=views.Unsubscribe.as_view(),
		name='unsubscribe',
	),
	path(
		route='<int:channel_id>/control',
		view=views.ChannelControl.as_view(),
		name='control',
	),
	path(
		route='<int:channel_id>/delete',
		view=views.ChannelDeleteView.as_view(),
		name='delete',
	),
	path(
		route='<int:channel_id>/members',
		view=views.ChannelMembers.as_view(),
		name='members',
	),
	path(
		route='about',
		view=views.About.as_view(),
		name='about',
	),
]
