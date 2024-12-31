from django.http import HttpResponseForbidden


class UserIsOwnerMixin:
	"""
	Миксин для проверки, что пользователь пытается изменить только свой профиль.
	"""
	def dispatch(self, request, *args, **kwargs):
		if kwargs.get('pk') and int(kwargs['pk']) != request.user.pk:
			return HttpResponseForbidden("Вы не можете изменять чужой профиль.")
		return super().dispatch(request, *args, **kwargs)
