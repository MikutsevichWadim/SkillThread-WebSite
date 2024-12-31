from django.db import models


class Question(
	models.Model
):
	test = models.ForeignKey(
		to='tests_tests.Test',
		related_name='questions',
		on_delete=models.CASCADE
	)
	text = models.CharField(
		max_length=255
	)


class QuestionOrder(
	models.Model
):
	test_attempt = models.ForeignKey(
		to='tests_tests.TestAttempt',
		related_name='question_orders',
		on_delete=models.CASCADE
	)
	question = models.ForeignKey(
		to='tests_questions.Question',
		related_name='question_orders',
		on_delete=models.CASCADE
	)
	order = models.IntegerField()
	
	class Meta:
		ordering = ['order']
		unique_together = ('test_attempt', 'question')
