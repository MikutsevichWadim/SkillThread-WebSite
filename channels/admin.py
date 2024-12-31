from django.contrib import admin

from channels.forms import ChannelForm
from channels.models import (
	Channel,
)


@admin.register(Channel)
class ChannelAdmin(
	admin.ModelAdmin,
):
	form = ChannelForm
