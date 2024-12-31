from django import forms

from channels.models import Channel


class ChannelForm(forms.ModelForm):
	name = forms.CharField(
		label='Название',
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
			},
		),
	)
	description = forms.CharField(
		label='Описание',
		widget=forms.Textarea(
			attrs={
				'class': 'form-control',
				'rows': 1,
			},
		),
		required=False
	)
	image = forms.FileField(
		label='Иконка канала',
		widget=forms.ClearableFileInput(
			attrs={
				'class': 'form-control channel-image',
			},
		),
		required=False
	)
	class Meta:
		model = Channel
		fields = [
			'image',
			'name',
			'description',
		]
