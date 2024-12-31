from crispy_forms.helper import FormHelper
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (
	AuthenticationForm,
	PasswordChangeForm,
	SetPasswordMixin,
	UserChangeForm,
	UserCreationForm,
)
from django.forms import ModelForm
from django.urls import reverse_lazy


class LoginUserForm(
	AuthenticationForm,
):
	username = forms.CharField(
		label='Логин',
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
			},
		),
	)
	password = forms.CharField(
		label='Пароль',
		widget=forms.PasswordInput(
			attrs={
				'class': 'form-control',
			},
		),
	)
	

class RegisterUserForm(
	UserCreationForm,
):
	username = forms.CharField(
		label='Логин',
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
			},
		),
	)
	email = forms.EmailField(
		label='Электронная почта',
		widget=forms.EmailInput(
			attrs={
				'class': 'form-control',
			},
		),
	)
	first_name = forms.CharField(
		label='Имя',
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
			},
		),
	)
	last_name = forms.CharField(
		label='Фамилия',
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
			},
		),
	)
	password1 = forms.CharField(
		label='Пароль',
		widget=forms.PasswordInput(
			attrs={
				'class': 'form-control',
			},
		),
	)
	password2 = forms.CharField(
		label='Повтор пароля',
		widget=forms.PasswordInput(
			attrs={
				'class': 'form-control',
			},
		),
	)
	
	class Meta:
		model = get_user_model()
		fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
	
	# def clean_repeat_password(self):
	# 	if self.cleaned_data['password'] != self.cleaned_data['repeat_password']:
	# 		raise forms.ValidationError('Пароли должны совпадать.')
	# 	return self.cleaned_data['repeat_password']
	#
	def clean_email(self):
		email = self.cleaned_data['email']
		if get_user_model().objects.filter(email=email).exists():
			raise forms.ValidationError(
				message='Такой электронный адрес уже используется',
			)
		return email
	
	
class CustomPasswordChangeForm(
	PasswordChangeForm,
):
	old_password = forms.CharField(
		label='Старый пароль',
		strip=False,
		widget=forms.PasswordInput(
			attrs={
				"autocomplete": "current-password",
				"autofocus": True,
				'class': 'form-control',
			}
		),
	)
	new_password1 = forms.CharField(
		label='Новый пароль',
		widget=forms.PasswordInput(
			attrs={
				'class': 'form-control',
			}
		),
	)
	new_password2 = forms.CharField(
		label='Подтверждение пароля',
		widget=forms.PasswordInput(
			attrs={
				'class': 'form-control',
			}
		),
	)
	
class UpdateUserForm(
	UserChangeForm,
):
	username = forms.CharField(
		label='Логин',
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
			},
		),
	)
	email = forms.EmailField(
		label='Электронная почта',
		widget=forms.EmailInput(
			attrs={
				'class': 'form-control',
			},
		),
	)
	first_name = forms.CharField(
		label='Имя',
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
			},
		),
	)
	last_name = forms.CharField(
		label='ф',
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
			},
		),
	)
	
	class Meta:
		model = get_user_model()
		fields = ['username', 'email', 'first_name', 'last_name']
