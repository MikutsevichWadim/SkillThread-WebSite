from django import template

register = template.Library()


@register.inclusion_tag(
	filename='channels/card.html'
)
def show_channel_card(
	channel,
	user,
):
	return {
		'channel': channel,
		'user': user,
	}
