from django import forms
from .models import TodoModel


class TodoForm(forms.ModelForm):
    title = forms.CharField(label='', 
        widget=forms.TextInput(attrs={'placeholder': 'Add title...'}
        )
    )
    content = forms.CharField(label='', 
        widget=forms.TextInput(attrs={'placeholder': 'Add Content...'}
        )
    )

    class Meta:
        model = TodoModel
        fields = '__all__'


class UpdateTodoForm(forms.ModelForm):
    title = forms.CharField(
        label='Edit title', widget=forms.TextInput(attrs={}))
    content = forms.CharField(
        label='Edit Content', widget=forms.TextInput(attrs={}))

    class Meta:
        model = TodoModel
        fields = '__all__'