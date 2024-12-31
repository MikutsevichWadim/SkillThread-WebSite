from django import forms
from django.forms import modelformset_factory

from tests_questions.forms import QuestionForm
from tests_questions.models import Question
from tests_tests.models import Test


class TestForm(
	forms.ModelForm
):
	class Meta:
		model = Test
		fields = ['title', 'description', 'duration']
