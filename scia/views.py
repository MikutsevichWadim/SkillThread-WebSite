import json

from django.http import JsonResponse
from django.views import View
from django.shortcuts import render
from django.middleware.csrf import get_token

class CookieView(View):
	"""
	Класс для работы с куки.
	"""

	def get(self, request):
		if request.headers.get('X-Requested-With') == 'XMLHttpRequest':  # Проверка AJAX-запроса
			cookie_value = request.COOKIES.get('example_cookie', 'Куки отсутствуют')
			return JsonResponse({'cookie_value': cookie_value})
		return render(request, 'cookie.html')

	def post(self, request):
		try:
			data = json.loads(request.body)  # Чтение данных из JSON
			cookie_value = data.get('cookie_value', 'Значение по умолчанию')
			response = JsonResponse({'message': 'Куки успешно установлены'})
			response.set_cookie(
				key='example_cookie',
				value=cookie_value,
				max_age=3600,
				httponly=True
			)
			return response
		except json.JSONDecodeError:
			return JsonResponse({'message': 'Неверный формат данных'}, status=400)
	
	def delete(self, request):
		# Удаление куки
		response = JsonResponse({'message': 'Куки удалены'})
		response.delete_cookie('example_cookie')
		return response

class DeleteCookieView(View):
	def post(self, request):
		response = JsonResponse({'message': 'Куки успешно удалены'})
		response.delete_cookie('example_cookie')
		return response


class SessionView(View):
	def post(self, request):
		try:
			data = json.loads(request.body)  # Чтение данных из JSON
			session_value = data.get('session_value', 'Значение по умолчанию')
			request.session['example_session'] = session_value
			return JsonResponse({'message': 'Сессия успешно установлена'})
		except json.JSONDecodeError:
			return JsonResponse({'message': 'Неверный формат данных'}, status=400)
	
	def get(self, request):
		if request.headers.get('X-Requested-With') == 'XMLHttpRequest':  # Проверка AJAX-запроса
			session_value = request.session.get('example_session', 'Сессия не установлена')
			return JsonResponse({'session_value': session_value})
		return render(request, 'session.html')
	
	def delete(self, request):
		try:
			del request.session['example_session']
			return JsonResponse({'message': 'Сессия успешно удалена'})
		except KeyError:
			return JsonResponse({'message': 'Сессия не найдена'}, status=404)
