import bleach
from django import forms

from posts.models import (
	AssignmentPost,
	LearningMaterialPost,
	Post,
)
from tests_tests.models import Test


# from tasks.models import Task


class PostForm(
	forms.ModelForm,
):
	class Meta:
		model = Post
		fields = [
			'title',
			'content',
		]
		
	title = forms.CharField(
		label='Заголовок',
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
			},
		),
	)
	content = forms.CharField(
		label="Содержимое (разрешённые теги: p, b, i, u, strong, ul, ol, li, br, code",
		widget=forms.Textarea(
			attrs={
				'class': 'form-control',
			},
		),
	)
	
	def clean_content(
		self
	):
		return bleach.clean(
			text=self.cleaned_data.get(
				'content'
			),
			tags=['p', 'b', 'i', 'u', 'strong', 'ul', 'ol', 'li', 'br', 'code'],
		)
	
	def save(self, commit=True):
		post = super().save(commit=False)
		if commit:
			post.save()  # Сохраняем пост, чтобы получить его ID
	
	# 	# Удаляем старые файлы
	#
	# 	AttachedFile.objects.filter(post=post).delete()
	#
	# 	# Сохраняем новые файлы
	# 	files = self.cleaned_data.get('files')
	# 	if files:
	# 		for file in files:
	# 			AttachedFile.objects.create(
	# 				post=post,
	# 				file=file,
	# 			)
	#
	# 	return post

class LearningMaterialPostForm(
	PostForm,
):
	class Meta(
		PostForm.Meta,
	):
		model = LearningMaterialPost
		fields = [
			'title',
			'content',
			'file',
		]

class AssignmentPostForm(
	PostForm,
):
	test = forms.ModelChoiceField(
		queryset=Test.objects.none(),
		required=False,
		label='Прикрепить тест (в разработке)',
		widget=forms.Select(
			attrs={
				'disabled': 'disabled',
			}
		)
	)
	# quiz = forms.ModelChoiceField(
	# 	queryset=Quiz.objects.all(),  # Изначально пустой queryset
	# 	required=False,  # Сделать необязательным, если не требуется
	# 	label='Выберите тест'
	# )
	
	class Meta(
		PostForm.Meta,
	):
		model = AssignmentPost
		fields = [
			'title',
			'content',
			# 'quiz',
			# 'task',
		]
		
	# def __init__(
	# 	self,
	# 	*args,
	# 	user=None,
	# 	channel=None,
	# 	**kwargs
	# ):
	# 	super().__init__(*args, **kwargs)
	# 	if user and channel:
	# 		self.fields['quiz'].queryset = Quiz.objects.filter(
	# 			created_by=user,
	# 			channel=channel,
	# 		)
	# 	else:
	# 		self.fields['quiz'].queryset = Quiz.objects.none()
