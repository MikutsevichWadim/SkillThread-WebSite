from django.urls import (
	path,
)

from scia.views import (
	CookieView,
	DeleteCookieView,
	SessionView,
)

app_name = 'scia'

urlpatterns = [
	path('cookie/', CookieView.as_view(), name='cookie_view'),
	path('session/', SessionView.as_view(), name='session_view'),
	path('cookie/delete/', DeleteCookieView.as_view(), name='delete_cookie_view'),
]
