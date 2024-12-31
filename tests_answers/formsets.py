from django.forms import (
	inlineformset_factory,
	modelformset_factory,
)

from tests_answers.forms import AnswerForm
from tests_answers.models import Answer
from tests_questions.models import Question

AnswerFormSet = inlineformset_factory(
	parent_model=Question,
	model=Answer,
	form=AnswerForm,
	extra=2,  # Количество пустых форм для новых ответов
	can_delete=True,
)
