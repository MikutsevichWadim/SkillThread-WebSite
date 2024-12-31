from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.timezone import now
from polymorphic.models import PolymorphicModel

from channels.models import (
	Channel,
)

# from tasks.models import Task


class Post(
	PolymorphicModel,
):
	channel = models.ForeignKey(
		to=Channel,
		on_delete=models.CASCADE,
		related_name='posts',
	)
	title = models.CharField(
		max_length=255,
	)
	content = models.TextField(
		blank=True,
		null=True,
	)
	created_at = models.DateTimeField(
		auto_now_add=True,
	)
	updated_at = models.DateTimeField(
		auto_now=True,
	)
	
	# METHODS
	
	def __str__(
		self
	):
		real_instance = self.get_real_instance()
		return (
			f'{real_instance.__class__.__name__}: '
			f'{self.title}'
		)
	
	def get_absolute_url(
		self
	):
		return reverse(
			viewname='posts:detail',
			kwargs={
				'post_id': self.pk,
			}
		)
	
	class Meta:
		ordering = ['-created_at']
		verbose_name = 'Пост'
		verbose_name_plural = 'Посты'


class LearningMaterialPost(
	Post,
):
	file = models.FileField(
		upload_to="posts/files/%Y/%m/%d/",
		verbose_name="Файл",
		null=True,
		blank=True,
	)


class AssignmentPost(
	Post,
):
	test = models.OneToOneField(
		to='tests_tests.Test',
		on_delete=models.SET_NULL,
		null=True,
		related_name='post',
	)
