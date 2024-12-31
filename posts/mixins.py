from django.core.exceptions import PermissionDenied
from django.http import HttpResponseForbidden
from django.shortcuts import (
	get_object_or_404,
	render,
)

from channels.models import Channel
from posts.models import Post

class PostOwnershipOrAuthorMixin:
	"""
	Миксин для проверки, что пользователь является создателем или автором канала.
	"""
	def dispatch(self, request, *args, **kwargs):
		channel = Channel.objects.get(pk=self.kwargs['channel_id'])
		
		# Проверяем, является ли пользователь создателем или автором канала
		if request.user != channel.created_by:
			return HttpResponseForbidden('У вас нет прав на добавление постов в этот канал')
		
		return super().dispatch(request, *args, **kwargs)


class PostMembershipRequiredMixin:
	def dispatch(self, request, *args, **kwargs):
		channel = Post.objects.get(pk=self.kwargs['post_id']).channel
		
		# Проверяем, является ли пользователь создателем или автором канала
		if request.user != channel.created_by and request.user not in channel.participants.all():
			return HttpResponseForbidden('Вы не можете просматривать посты в этом канале')
		
		return super().dispatch(request, *args, **kwargs)
	

class PostUpdateMixin:
	def dispatch(self, request, *args, **kwargs):
		# Получаем канал по ID, который передается в URL
		channel = Post.objects.get(pk=self.kwargs['pk']).channel
		
		# Проверяем, является ли пользователь создателем или автором канала
		if request.user != channel.created_by and request.user not in channel.authors.all():
			return HttpResponseForbidden('Вы не можете редактировать посты в этом канале')
		
		return super().dispatch(request, *args, **kwargs)


class PostDeleteMixin:
	def dispatch(self, request, *args, **kwargs):
		# Получаем канал по ID, который передается в URL
		channel = Post.objects.get(pk=self.kwargs['pk']).channel
		
		# Проверяем, является ли пользователь создателем или автором канала
		if request.user != channel.created_by and request.user not in channel.authors.all():
			return HttpResponseForbidden('Вы не можете удалять посты в этом канале')
		
		return super().dispatch(request, *args, **kwargs)
