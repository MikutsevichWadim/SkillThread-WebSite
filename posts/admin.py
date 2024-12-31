from django.contrib import admin
from polymorphic.admin import (
	PolymorphicChildModelAdmin,
	PolymorphicParentModelAdmin,
)

from posts.models import (
	AssignmentPost,
	LearningMaterialPost,
	Post,
)


@admin.register(Post)
class PostAdmin(
	PolymorphicParentModelAdmin,
):
	base_model = Post
	child_models = (
		LearningMaterialPost,
		AssignmentPost,
	)


@admin.register(LearningMaterialPost)
class LearningMaterialPostAdmin(
	PolymorphicChildModelAdmin,
):
	base_model = Post


@admin.register(AssignmentPost)
class AssignmentPostAdmin(
	PolymorphicChildModelAdmin,
):
	base_model = Post
