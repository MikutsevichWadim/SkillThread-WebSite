from django import template

register = template.Library()


@register.inclusion_tag(
	filename='posts/card.html'
)
def show_post_card(
	post,
):
	return {
		'post': post,
	}


@register.inclusion_tag(
	filename='posts/comment.html',
)
def show_comment(
	comment,
	user,
):
	return {
		'comment': comment,
		'user': user,
	}


@register.inclusion_tag(
	filename='posts/icon.html',
)
def show_post_icon(
	post,
	icon_width,
):
	return {
		'post': post,
		'icon_width': icon_width,
	}
