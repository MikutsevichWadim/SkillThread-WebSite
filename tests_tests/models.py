from django.contrib.auth import get_user_model
from django.db import models


class Test(
	models.Model
):
	title = models.CharField(
		max_length=255
	)
	description = models.TextField()
	duration = models.DurationField(
		null=True,
		blank=True,
	)
	created_at = models.DateTimeField(
		auto_now_add=True
	)
	updated_at = models.DateTimeField(
		auto_now=True
	)


class TestAttempt(
	models.Model
):
	user = models.ForeignKey(
		to=get_user_model(),
		related_name='test_attempts',
		on_delete=models.CASCADE
	)
	test = models.ForeignKey(
		to='tests_tests.Test',
		related_name='attempts',
		on_delete=models.CASCADE
	)
	started_at = models.DateTimeField(
		auto_now_add=True
	)
	completed_at = models.DateTimeField(
		null=True,
		blank=True
	)
	status = models.CharField(
		max_length=50,
		choices=[
			('in_progress', 'In Progress'),
			('completed', 'Completed'),
		],
	)
	score = models.FloatField(
		null=True,
		blank=True
	)
	current_question = models.ForeignKey(
		to='tests_questions.Question',
		related_name='current_attempts',
		null=True,
		blank=True,
		on_delete=models.SET_NULL
	)


class TestResult(
	models.Model
):
	test_attempt = models.ForeignKey(
		to='tests_tests.TestAttempt',
		on_delete=models.CASCADE
	)
	total_score = models.FloatField()
	passed = models.BooleanField(
		default=False
	)
	# feedback = models.TextField(
	# 	null=True,
	# 	blank=True
	# )
