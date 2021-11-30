from django import forms
from .models import TodoModel
class TodoForm(forms.ModelForm):
	class Meta:
		model = TodoModel
		fields = ['task','deadline','Note','user']
		widgets = {
			'task': forms.Textarea(attrs={'rows':4, 'cols':21}),
			'Note': forms.Textarea(attrs={'rows':4, 'cols':21}),
			'user': forms.TextInput(attrs={'value':'', 'id':'uid','type':'hidden'}),
        	}