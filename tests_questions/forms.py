from django import forms

from tests_questions.models import Question


class QuestionForm(forms.ModelForm):
	class Meta:
		model = Question
		fields = ['text']
