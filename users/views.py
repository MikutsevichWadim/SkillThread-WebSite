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
from django.core.mail import send_mail  # Import send_mail
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
from skillthread import settings
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
	
	def form_invalid(self, form):
		email = form.data.get('email')
		
		# Check if email already exists
		if get_user_model().objects.filter(email=email).exists():
			
			messages.error(self.request, 'Такой электронный адрес уже используется')
		
		return super().form_invalid(form)
	
	
	
	def get_success_url(self):
		messages.success(
			request=self.request,
			message='Вы успешно зарегистрированы!',
		)
	
		# Access the validated email from the form's cleaned_data
		email = self.request.POST.get('email')  # Access the email from the request POST data (safe fallback)
		
		subject = 'Привет'
		message = 'Добро пожаловать на наш сайт'
		from_email = settings.EMAIL_HOST_USER  # Replace with your "from" email address
		recipient_list = [email]
		
		try:
			send_mail(subject, message, from_email, recipient_list, fail_silently=False)
		except Exception as e:
			messages.error(self.request, f"Ошибка отправки письма: {e}")  # Log the error
		
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
