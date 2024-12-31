from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.http import (
	HttpRequest,
	HttpResponse,
)
from django.shortcuts import (
	get_object_or_404,
	redirect,
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
	DetailView,
	ListView,
	TemplateView,
	UpdateView,
)

from channels.forms import ChannelForm
from channels.mixins import (
	ChannelCreatorRequired2Mixin,
	ChannelMembershipRequiredMixin,
	ChannelParticipantRequiredMixin,
	ChannelCreatorRequiredMixin,
)
from channels.models import Channel

app_name = 'channels'


class ChannelPosts(
	LoginRequiredMixin,
	ChannelMembershipRequiredMixin,
	View,
):
	template_name = 'channels/post-list.html'
	
	def get(
		self,
		request,
		channel_id
	):
		channel = get_object_or_404(
			klass=Channel,
			pk=channel_id,
		)
		post_list = channel.posts.all()
		paginator = Paginator(
			object_list=post_list,
			per_page=10,
		)
		page_number = request.GET.get(
			'page'
		)
		page_obj = paginator.get_page(
			page_number
		)
		context = {
			'channel': channel,
			'page_obj': page_obj,
		}
		return render(
			request=request,
			template_name=self.template_name,
			context=context,
		)


class SearchChannels(
	ListView,
):
	model = Channel
	template_name = 'channels/search.html'
	context_object_name = 'channel_list'
	paginate_by = 10
	
	def get_queryset(
		self
	):
		return (
			Channel.popular
			.popular_channels()
			.filter(
				name__icontains=self.request.GET.get(
					'q',
					'',
				),
			)
		)
	
	def get_context_data(
		self,
		*,
		object_list=...,
		**kwargs
	):
		context = super().get_context_data(
			**kwargs
		)
		context['q'] = self.request.GET.get(
			'q'
		)
		return context


class ChannelDetail(
	DetailView,
):
	model = Channel
	template_name = 'channels/detail.html'
	
	def get_object(
		self,
		queryset=None
		):
		channel = super().get_object(
			queryset
		)
		channel.increment_visits()
		return channel


class CreateChannel(
	LoginRequiredMixin,
	CreateView,
):
	model = Channel
	form_class = ChannelForm
	template_name = 'channels/create.html'
	extra_context = {
		'form_title': 'Создание канала',
		'submit_button_inner': 'Создать',
	}
	
	def form_valid(
		self,
		form
	):
		form.instance.created_by = self.request.user
		return super().form_valid(
			form
		)
	
	def get_success_url(
		self
	):
		print(
			self.object.pk
		)
		return reverse(
			viewname='channels:detail',
			kwargs={
				'pk': self.object.pk,
			},
		)


class UpdateChannel(
	LoginRequiredMixin,
	ChannelCreatorRequiredMixin,
	UpdateView,
):
	model = Channel
	form_class = ChannelForm
	template_name = 'channels/update.html'
	extra_context = {
		'form_title': 'Редактирование канала',
		'submit_button_inner': 'Сохранить',
	}
	
	def get_success_url(
		self
	):
		return reverse(
			viewname='channels:detail',
			kwargs={
				'pk': self.object.pk,
			},
		)
	
	def get_object(
		self,
		queryset=...
		):
		channel_id = self.kwargs.get(
			'channel_id'
		)
		return get_object_or_404(
			klass=Channel,
			pk=channel_id,
		)


class UserChannels(
	LoginRequiredMixin,
	TemplateView,
):
	template_name = 'channels/of-user.html'


class Subscribe(
	LoginRequiredMixin,
	View,
):
	def post(
		self,
		request: HttpRequest,
		channel_id: int,
	) -> HttpResponse:
		channel = get_object_or_404(
			klass=Channel,
			pk=channel_id,
		)
		
		channel.participants.add(
			request.user
		)
		
		return redirect(
			to='channels:detail',
			pk=channel.pk,
		)


class Unsubscribe(
	LoginRequiredMixin,
	ChannelParticipantRequiredMixin,
	View,
):
	def post(
		self,
		request: HttpRequest,
		channel_id: int,
	) -> HttpResponse:
		channel = get_object_or_404(
			klass=Channel,
			pk=channel_id,
		)
		
		channel.participants.remove(
			request.user
		)
		
		return redirect(
			to='channels:detail',
			pk=channel.pk,
		)


class ChannelControl(
	LoginRequiredMixin,
	ChannelCreatorRequired2Mixin,
	View,
):
	template_name = 'channels/control.html'
	
	def get(
		self,
		request: HttpRequest,
		channel_id: int,
	) -> HttpResponse:
		channel = get_object_or_404(
			klass=Channel,
			pk=channel_id,
		)
		context = {
			'channel': channel,
		}
		
		return render(
			request=request,
			template_name=self.template_name,
			context=context,
		)

class ChannelDeleteView(
	LoginRequiredMixin,
	ChannelCreatorRequiredMixin,
	DeleteView,
):
	model = Channel
	template_name = 'channels/delete.html'
	success_url = reverse_lazy(
		'channels:of-user'
	)
	
	def get_object(
		self,
		queryset=None
		):
		# Получаем channel_id из URL
		channel_id = self.kwargs.get(
			'channel_id'
		)
		# Получаем объект канала по channel_id
		return get_object_or_404(
			Channel,
			pk=channel_id
		)


class ChannelMembers(
	LoginRequiredMixin,
	ChannelMembershipRequiredMixin,
	TemplateView,
):
	template_name = 'channels/members.html'
	
	def get_context_data(
		self,
		**kwargs
		):
		context = super().get_context_data(
			**kwargs
		)
		
		context['channel'] = Channel.objects.get(
			pk=self.kwargs['channel_id']
		)
		
		return context
	
class About(
	TemplateView,
):
	template_name = 'channels/about.html'


class ChannelQuizes(
	View,
):
	template_name = 'channels/quizes.html'
	def get(
		self,
		request: HttpRequest,
		channel_id: int,
	) -> HttpResponse:
		channel = get_object_or_404(
			klass=Channel,
			id=channel_id,
		)
		post_list = channel.quizes.all()
		paginator = Paginator(
			object_list=post_list,
			per_page=10,
		)
		page_number = request.GET.get(
			'page'
		)
		page_obj = paginator.get_page(
			page_number
		)
		context = {
			'channel': channel,
			'page_obj': page_obj,
		}
		return render(
			request=request,
			template_name=self.template_name,
			context=context,
		)


class ChannelQuestions(
	View,
):
	template_name = 'channels/questions.html'
	def get(
		self,
		request: HttpRequest,
		channel_id: int,
	) -> HttpResponse:
		channel = get_object_or_404(
			klass=Channel,
			id=channel_id,
		)
		questions = channel.questions.all()
		paginator = Paginator(
			object_list=questions,
			per_page=10,
		)
		page_number = request.GET.get(
			'page'
		)
		page_obj = paginator.get_page(
			page_number
		)
		context = {
			'channel': channel,
			'page_obj': page_obj,
		}
		return render(
			request=request,
			template_name=self.template_name,
			context=context,
		)
