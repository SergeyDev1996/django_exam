from django import forms
from django.forms import ModelForm

from to_do_list.models import Task


class DateInput(forms.DateInput):
    input_type = 'date'


class TaskForm(ModelForm):

    class Meta:
        model = Task
        widgets = {
            'made_on': DateInput(),
        }
        fields = "__all__"