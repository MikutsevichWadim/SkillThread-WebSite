from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class ChannelMembersManager(models.Manager):
	def get_channel_members(self, channel_id):
		# Получаем канал по id
		channel = self.get(id=channel_id)
		
		# Создаем список всех пользователей, связанных с каналом
		users = set()
		
		# Добавляем создателя канала
		users.add(channel.created_by)
		
		# Добавляем авторов канала
		users.update(channel.authors.all())
		
		# Добавляем участников канала
		users.update(channel.participants.all())
		
		return users


class ChannelPopularManager(models.Manager):
	def popular_channels(self):
		return self.order_by('-visits_count')


class Channel(
	models.Model,
):
	# MANAGERS
	objects = models.Manager()
	popular = ChannelPopularManager()
	objects_members = ChannelMembersManager()
	
	# FIELDS
	created_by = models.ForeignKey(
		to=get_user_model(),
		related_name='created_channels',
		on_delete=models.SET_NULL,
		null=True,
	)
	# authors = models.ManyToManyField(
	# 	to=get_user_model(),
	# 	related_name='author_channels',
	# )
	participants = models.ManyToManyField(
		to=get_user_model(),
		related_name='participant_channels',
	)
	image = models.ImageField(
		upload_to='channels/image',
		default='default-channel-image.svg'
	)
	name = models.CharField(
		max_length=255,
		null=False,
	)
	description = models.TextField(
		blank=True,
	)
	visits_count = models.PositiveIntegerField(
		default=0,
	)
	
	def __str__(
		self,
	) -> str:
		return self.name
	
	def increment_visits(self):
		self.visits_count += 1
		self.save()
	
	def get_absolute_url(
		self
	):
		return reverse(
			viewname='channels:detail',
			kwargs={
				'pk': self.id,
			},
		)
	
	class Meta:
		verbose_name = 'Канал'
		verbose_name_plural = 'Каналы'



# class ChannelLink(models.Model):
# 	channel = models.ForeignKey(
# 		to=Channel,
# 		on_delete=models.CASCADE,
# 		related_name="channels_links",
# 	)
# 	url = models.URLField(
# 		max_length=2000,
# 	)
# 	text = models.CharField(
# 		max_length=255,
# 	)
#
# 	def __str__(self):
# 		return self.url
#
# 	class Meta:
# 		verbose_name = 'Ссылка канала'
# 		verbose_name_plural = 'Ссылки каналов'
