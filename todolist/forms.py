from django import forms
from .models import ToDoList
from email.policy import default

class ToDo(forms.Form):
    name = forms.CharField(label = "Name", required = True)
    description = forms.CharField(label = "Description", required = True)

class updateToDo(forms.ModelForm):
    class Meta:
        model = ToDoList
        fields = ['is_finished']