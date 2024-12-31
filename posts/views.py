from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import (
	HttpRequest,
	HttpResponse,
)
from django.shortcuts import (
	get_object_or_404,
	render,
)
from django.urls import (
	reverse,
	reverse_lazy,
)
from django.views import View
from django.views.generic import (
	CreateView,
	DeleteView,
	UpdateView,
)


from channels.models import Channel

from . import mixins as posts_mixins
from .forms import (
	AssignmentPostForm,
	LearningMaterialPostForm,
	PostForm,
)
from .models import (
	AssignmentPost,
	LearningMaterialPost,
	Post,
)


class ShowPost(
	LoginRequiredMixin,
	posts_mixins.PostMembershipRequiredMixin,
	View,
):
	template_name = 'posts/detail.html'
	
	def get(
		self,
		request: HttpRequest,
		post_id: int,
	) -> HttpResponse:
		post = get_object_or_404(
			klass=Post,
			pk=post_id,
		)
		context = {
			'post': post,
		}
		return render(
			request=request,
			template_name=self.template_name,
			context=context,
		)
	

class CreatePost(
	LoginRequiredMixin,
	posts_mixins.PostOwnershipOrAuthorMixin,
	CreateView,
):
	model = Post
	form_class = PostForm
	template_name = 'posts/create.html'

	def form_valid(self, form):
		channel = get_object_or_404(
			klass=Channel,
			id=self.kwargs['channel_id'],
		)
		
		# Устанавливаем канал для нового поста
		form.instance.channel = channel
		
		return super().form_valid(form)
	
	def get_success_url(self):
		# Перенаправление после успешного создания поста
		return reverse_lazy('channels:post-list', kwargs={'channel_id': self.object.channel.id})
	
	
# class UpdatePost(
# 	LoginRequiredMixin,
# 	posts_mixins.PostUpdateMixin,
# 	UpdateView,
# ):
# 	model = Post
# 	form_class = PostForm
# 	template_name = 'app/form.html'
# 	extra_context = {
# 		'form_title': 'Изменение поста',
# 		'submit_button_inner': 'Сохранить изменения',
# 	}
#
# 	def get_success_url(self):
# 		return reverse_lazy('posts:detail', kwargs={'post_id': self.object.id})


class PostDeleteView(
	LoginRequiredMixin,
	posts_mixins.PostDeleteMixin,
	DeleteView,
):
	model = Post
	template_name = 'posts/delete.html'
	context_object_name = 'post'
	
	def get_success_url(self):
	# Возвращаем URL для списка постов данного канала
		return reverse_lazy('channels:post-list', kwargs={'channel_id': self.object.channel.id})


class CreateLearningMaterialPost(
	CreateView,
):
	template_name = 'app/form.html'
	model = LearningMaterialPost
	form_class = LearningMaterialPostForm
	extra_context = {
		'form_title': 'Добавление учебного материала',
		'submit_button_inner': 'Создать',
	}
	
	def form_valid(self, form):
		channel_id = self.kwargs['channel_id']
		form.instance.channel_id = channel_id
		response = super().form_valid(form)
		return response
	
	def get_success_url(self):
		channel_id = self.kwargs['channel_id']
		return reverse(
			viewname='channels:post-list',
			kwargs={
				'channel_id': channel_id
			},
		)


class CreateAssignmentPost(
	CreateView,
):
	template_name = 'app/form.html'
	model = AssignmentPost
	form_class = AssignmentPostForm
	extra_context = {
		'form_title': 'Добавление теста',
		'submit_button_inner': 'Создать',
	}
	
	def form_valid(self, form):
		channel_id = self.kwargs['channel_id']
		form.instance.channel_id = channel_id
		response = super().form_valid(form)
		return response
	
	def get_success_url(self):
		channel_id = self.kwargs['channel_id']
		return reverse(
			viewname='channels:post-list',
			kwargs={
				'channel_id': channel_id
			},
		)


class UpdateAssignmentPost(
	UpdateView,
):
	template_name = 'app/form.html'
	model = AssignmentPost
	form_class = AssignmentPostForm
	extra_context = {
		'form_title': 'Обновление поста',
		'submit_button_inner': 'Обновить',
	}
	
	def get_success_url(self):
		post_id = self.kwargs['pk']
		return reverse(
			viewname='posts:detail',
			kwargs={
				'post_id': post_id
			},
		)


class UpdateLearningMaterialPost(
	UpdateView,
):
	template_name = 'app/form.html'
	model = LearningMaterialPost
	form_class = LearningMaterialPostForm
	extra_context = {
		'form_title': 'Обновление поста',
		'submit_button_inner': 'Обновить',
	}
	
	def get_success_url(self):
		post_id = self.kwargs['pk']
		return reverse(
			viewname='posts:detail',
			kwargs={
				'post_id': post_id
			},
		)
