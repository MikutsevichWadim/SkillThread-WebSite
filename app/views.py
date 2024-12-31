from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.http import (
	HttpRequest,
	HttpResponse,
)
from django.shortcuts import (
	get_object_or_404,
	render,
)
from django.views import View
from django.views.generic import ListView

from channels.models import Channel
from posts.models import Post


class Index(
	ListView,
):
	model = Channel
	template_name = 'app/index.html'
	context_object_name = 'channel_list'
	paginate_by = 10
	
	def get_queryset(
		self
	):
		return Channel.popular.popular_channels()


class ErrorHandlerView(
	View
):
	template_name = 'app/error-base.html'  # Используем общий шаблон
	
	def get_context_data(
		self,
		error_code,
		error_message
	):
		return {
			'error_code': error_code,
			'error_message': error_message,
		}
	
	def get(
		self,
		request,
		*args,
		**kwargs
	):
		error_code = kwargs.get(
			'error_code',
			500
		)  # Код ошибки по умолчанию 500
		if error_code == 404:
			error_message = 'Страница не найдена'
		elif error_code == 500:
			error_message = 'Произошла ошибка на сервере'
		else:
			error_message = 'Неизвестная ошибка'
		
		context = self.get_context_data(
			error_code=error_code,
			error_message=error_message
		)
		return render(
			request,
			self.template_name,
			context,
			status=error_code
		)
