from django import forms
from .models import todolists


class TodoForm(forms.ModelForm):
	class Meta:
		model = todolists
		fields = "__all__"
