import os

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


def user_avatar_path(instance, filename):
	return os.path.join('avatars', str(instance.id))


class User(
	AbstractUser,
):
	photo = models.ImageField(
		upload_to=user_avatar_path,
		blank=True,
		null=True,
		verbose_name='Аватарка',
	)
	
	class Meta:
		verbose_name = 'Пользователь'
		verbose_name_plural = 'Пользователи'
		
	def get_absolute_url(self):
		return reverse(
			viewname='users:detail',
			kwargs={
				'pk': self.id,
			},
		)
