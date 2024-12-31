import importlib

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


@register.inclusion_tag(
	filename='app/include/form-footer.html'
)
def show_form_footer(
	submit_button_inner,
):
	return {
		'submit_button_inner': submit_button_inner,
	}


@register.inclusion_tag(
	filename='app/include/form-header.html'
)
def show_form_header(
	form_title,
):
	return {
		'form_title': form_title,
	}

@register.filter(name='is_instance_of')
def is_instance_of(value, class_path):
	try:
		# Разбиваем строку на модуль и класс
		module_name, class_name = class_path.rsplit('.', 1)
		
		# Динамически импортируем модуль
		module = importlib.import_module(module_name)
		
		# Получаем класс из модуля
		class_ = getattr(module, class_name)
		
		# Проверяем, является ли объект экземпляром этого класса
		return isinstance(value, class_)
	except KeyError:
		return False
