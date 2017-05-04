from django import forms
from models import Flow


class FlowPost(forms.ModelForm):
	class Meta:
		model = Flow
		fields = ('name', 'recurrence')
