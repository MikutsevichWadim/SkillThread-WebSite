from django import forms

from tests_answers.models import Answer


class AnswerForm(forms.ModelForm):
	class Meta:
		model = Answer
		fields = ['text', 'is_correct']
