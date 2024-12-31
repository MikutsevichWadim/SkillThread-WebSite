from django.db import transaction
from django.forms import modelformset_factory
from django.http import HttpResponse
from django.shortcuts import (
	redirect,
	render,
)
from django.views import View
from django.views.generic import ListView

from tests_answers.forms import AnswerForm
from tests_answers.formsets import AnswerFormSet
from tests_answers.models import Answer
from tests_questions.forms import QuestionForm
from tests_questions.formsets import QuestionFormSet
from tests_questions.models import Question
from tests_tests.forms import TestForm
from tests_tests.models import Test


class TestCreateView(
	View
):
	def get(self, request):
		return render(
			request=request,
			template_name='tests_tests/create.html',
		)
	
	def post(self, request):
		print(request.POST)
		return HttpResponse(code=200)
# 	def get(self, request, *args, **kwargs):
# 		test_form = TestForm()
#
# 		# Формы для вопросов
# 		question_formset = QuestionFormSet(queryset=Question.objects.none())
#
# 		# Формы для ответов
# 		answer_formsets = [AnswerFormSet(queryset=Answer.objects.none(), prefix=f'answers_{i}') for i in range(question_formset.total_form_count())]
#
# 		return render(
# 			request,
# 			'tests_tests/create_test.html',
# 			{'test_form': test_form, 'question_formset': question_formset, 'answer_formsets': answer_formsets}
# 		)
#
# 	def post(self, request, *args, **kwargs):
# 		test_form = TestForm(request.POST)
#
# 		# Обработка вопросов
# 		question_formset = QuestionFormSet(request.POST)
#
# 		# Обработка ответов
# 		answer_formsets = [AnswerFormSet(request.POST, prefix=f'answers_{i}') for i in range(question_formset.total_form_count())]
#
# 		if test_form.is_valid() and question_formset.is_valid() and all(formset.is_valid() for formset in answer_formsets):
# 			# Начинаем транзакцию для атомарности
# 			with transaction.atomic():
# 				test = test_form.save()
#
# 				# Сохраняем вопросы
# 				for question_form in question_formset:
# 					question = question_form.save(commit=False)
# 					question.test = test
# 					question.save()
#
# 					# Сохраняем ответы для каждого вопроса
# 					for answer_form in answer_formsets[question_formset.forms.index(question_form)]:
# 						answer = answer_form.save(commit=False)
# 						answer.question = question
# 						answer.save()
#
# 				return redirect('tests_tests:test_detail', pk=test.pk)
#
# 		return render(
# 			request,
# 			'tests_tests/create_test.html',
# 			{'test_form': test_form, 'question_formset': question_formset, 'answer_formsets': answer_formsets}
# 		)
#
# def test(request):
# 	return render(request, 'test.html')
