from django.db import models


class Answer(
	models.Model
):
	question = models.ForeignKey(
		to='tests_questions.Question',
		related_name='answers',
		on_delete=models.CASCADE,
	)
	text = models.CharField(
		max_length=255,
	)
	is_correct = models.BooleanField(
		default=False,
	)

class AnswerResponse(
	models.Model
):
	test_attempt = models.ForeignKey(
		to='tests_tests.TestAttempt',
		related_name='responses',
		on_delete=models.CASCADE,
	)
	question = models.ForeignKey(
		to='tests_questions.Question',
		on_delete=models.CASCADE,
	)
	selected_answer = models.ForeignKey(
		to='tests_answers.Answer',
		null=True,
		blank=True,
		on_delete=models.SET_NULL,
	)
	
	class Meta:
		unique_together = ('test_attempt', 'question')

class AnswerOrder(models.Model):
	test_attempt = models.ForeignKey(
		to='tests_tests.TestAttempt',
		related_name='answer_orders',
		on_delete=models.CASCADE
	)
	answer = models.ForeignKey(
		to='tests_answers.Answer',
		related_name='answer_orders',
		on_delete=models.CASCADE
	)
	order = models.IntegerField()  # Порядок выбранного ответа для данного пользователя
	
	class Meta:
		ordering = ['order']  # Порядок ответов по возрастанию order
		unique_together = ('test_attempt', 'answer')  # Уникальность по пользователю,
	# ответу и ответу пользователя
