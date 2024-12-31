from django.http import (
	Http404,
	HttpResponseForbidden,
)
from django.shortcuts import get_object_or_404

from channels.models import Channel


class ChannelCreatorRequiredMixin:
	"""
	Миксин для проверки, что объект принадлежит текущему пользователю.
	Если объект не принадлежит пользователю, то будет возвращен ответ 403 (Forbidden).
	"""
	def dispatch(self, request, *args, **kwargs):
		# Получаем объект, к которому осуществляется доступ
		obj = self.get_object()  # Получение объекта через стандартный метод get_object
		# Проверяем, что объект принадлежит текущему пользователю
		if obj.created_by != request.user:
			# Возвращаем ответ с ошибкой 403, если объект не принадлежит пользователю
			return HttpResponseForbidden("Вы не имеете прав доступа к этому объекту.")
		# Если проверка прошла успешно, передаем управление дальше
		return super().dispatch(request, *args, **kwargs)


class ChannelParticipantRequiredMixin:
	"""
	Миксин для проверки, что объект принадлежит текущему пользователю.
	"""
	def dispatch(self, request, *args, **kwargs):
		# Получаем канал по ID, который передается в URL
		channel = get_object_or_404(Channel, id=kwargs['channel_id'])
		
		# Проверяем, является ли текущий пользователь участником канала
		if not channel.participants.filter(id=request.user.id).exists():
			return HttpResponseForbidden("Вы не являетесь участником этого канала.")
		
		return super().dispatch(request, *args, **kwargs)

class ChannelCreatorRequired2Mixin:
	"""
	Миксин для проверки, что объект принадлежит текущему пользователю.
	Если объект не принадлежит пользователю, то будет возвращен ответ 403 (Forbidden).
	"""
	def dispatch(self, request, *args, **kwargs):
		# Извлекаем channel_id из URL
		channel_id = kwargs.get('channel_id')
		
		# Получаем объект канала через get_object_or_404
		channel = get_object_or_404(Channel, pk=channel_id)
		
		# Проверяем, что канал принадлежит текущему пользователю
		if channel.created_by != request.user:
			# Возвращаем ответ с ошибкой 403, если объект не принадлежит пользователю
			return HttpResponseForbidden("Вы не имеете прав доступа к этому объекту.")
		
		# Если проверка прошла успешно, передаем управление дальше
		return super().dispatch(request, *args, **kwargs)


class ChannelMembershipRequiredMixin:
	"""
	Миксин для проверки, что объект принадлежит текущему пользователю.
	"""
	def dispatch(self, request, *args, **kwargs):
		# Получаем канал по ID, который передается в URL
		channel = get_object_or_404(Channel, id=kwargs['channel_id'])
		
		if request.user not in {channel.created_by, *channel.participants.all()}:
			return HttpResponseForbidden("Вы не являетесь участником этого канала.")
		
		return super().dispatch(request, *args, **kwargs)
