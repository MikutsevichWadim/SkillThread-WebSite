from django.contrib import messages
from django.contrib.auth import (
	authenticate,
	get_user_model,
	login,
	logout,
)
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (
	LoginView,
	PasswordChangeDoneView,
	PasswordChangeView,
)
from django.http import (
	HttpRequest,
	HttpResponse,
	HttpResponseRedirect,
)
from django.shortcuts import render
from django.urls import (
	reverse,
	reverse_lazy,
)
from django.views import View
from django.views.generic import (
	CreateView,
	DetailView,
	ListView,
	UpdateView,
)

from channels.models import Channel
from . import forms
from .forms import (
	CustomPasswordChangeForm,
	UpdateUserForm,
)
from .mixins import UserIsOwnerMixin


class LoginUser(
	LoginView,
):
	form_class = forms.LoginUserForm
	template_name = 'app/form.html'
	extra_context = {
		'form_title': 'Вход в аккаунт',
		'submit_button_inner': 'Войти',
	}

class RegisterUser(
	CreateView,
):
	form_class = forms.RegisterUserForm
	template_name = 'app/form.html'
	success_url = reverse_lazy('users:login')
	extra_context = {
		'form_title': 'Регистрация',
		'submit_button_inner': 'Создать аккаунт',
	}
	
	def get_success_url(self):
		messages.success(
			request=self.request,
			message='Вы успешно зарегистрированы!',
		)
		return super().get_success_url()


class UserDetailView(
	LoginRequiredMixin,
	DetailView,
):
	model = get_user_model()
	template_name = 'users/detail.html'
	

class UserUpdateView(
	LoginRequiredMixin,
	UserIsOwnerMixin,
	UpdateView,
):
	model = get_user_model()
	template_name = 'users/update.html'
	form = UpdateUserForm
	fields = [
		'username',
		'email',
		'first_name',
		'last_name',
	]
	extra_context = {
		'form_title': 'Изменение профиля',
		'submit_button_inner': 'Сохранить',
	}
	def get_success_url(self):
		return reverse(
			viewname='users:detail',
			kwargs={
				'pk': self.object.pk,
			}
		)
	

class CustomPasswordChangeView(
	LoginRequiredMixin,
	UserIsOwnerMixin,
	PasswordChangeView,
):
	form_class = CustomPasswordChangeForm
	template_name = 'users/password-change.html'
	extra_context = {
		'form_title': 'Смена пароля',
		'submit_button_inner': 'Изменить пароль',
	}
	success_url = reverse_lazy(
		viewname='users:password-change-done',
	)


class CustomPasswordChangeDoneView(
	PasswordChangeDoneView,
):
	template_name = 'users/password-change-done.html'
