from django.conf.urls.static import static
from django.contrib import admin
from django.urls import (
	path,
	include,
)

from . import settings

urlpatterns = [
	path(
		route='admin/',
		view=admin.site.urls,
	),
	
	path(
		route='',
		view=include(
			arg='app.urls',
		),
	),
	path(
		route='users/',
		view=include(
			arg='users.urls',
			namespace='users',
		),
	),
	path(
		route='channels/',
		view=include(
			arg='channels.urls',
			namespace='channels',
		),
	),
	path(
		route='posts/',
		view=include(
			arg='posts.urls',
			namespace='posts',
		),
	),
	path(
		route='tests/',
		view=include(
			arg='tests_tests.urls',
			namespace='tests',
		),
	),
	path(
		route='',
		view=include(
			arg='scia.urls',
		),
	),
]

if settings.DEBUG:
	urlpatterns += static(
		settings.MEDIA_URL,
		document_root=settings.MEDIA_ROOT
	)
