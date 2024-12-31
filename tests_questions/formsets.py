from django.forms import (
	inlineformset_factory,
	modelformset_factory,
)

from tests_answers.formsets import AnswerFormSet
from tests_questions.forms import QuestionForm
from tests_questions.models import Question

from django import forms

from tests_tests.models import Test


class BaseQuestionFormSet(forms.BaseInlineFormSet):
	def __init__(self, *args, **kwargs):
		self.nested_formsets = []
		super().__init__(*args, **kwargs)
		# Создание вложенных AnswerFormSet для каждого вопроса
		for question_form in self.forms:
			instance = question_form.instance
			question_form.nested_formset = AnswerFormSet(
				instance=instance,
				prefix=f"answers_{question_form.prefix}",
				data=kwargs.get('data') if question_form.is_bound else None,
				files=kwargs.get('files') if question_form.is_bound else None,
			)
			self.nested_formsets.append(question_form.nested_formset)
	
	def is_valid(self):
		if not super().is_valid():
			return False
		# Проверка валидности вложенных AnswerFormSet
		for nested_formset in self.nested_formsets:
			if not nested_formset.is_valid():
				return False
		return True
	
	def save(self, commit=True):
		# Сохраняем вопросы
		instances = super().save(commit=commit)
		for form, instance in zip(self.forms, instances):
			# Сохраняем ответы для каждого вопроса
			form.nested_formset.instance = instance
			form.nested_formset.save(commit=commit)
		return instances

QuestionFormSet = inlineformset_factory(
	parent_model=Test,
	model=Question,
	form=QuestionForm,
	formset=BaseQuestionFormSet,
	extra=1,
	can_delete=True,
)
