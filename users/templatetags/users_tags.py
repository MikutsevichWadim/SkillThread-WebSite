from django import template

register = template.Library()


@register.inclusion_tag(
	filename='users/inclusion/inline.html'
)
def show_user_inline(
	user,
):
	return {
		'user': user,
	}
