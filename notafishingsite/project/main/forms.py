from .models import Job
from django.forms import ModelForm, TextInput, Textarea


class JobForm(ModelForm):
    class Meta:
        model = Job
        fields = ["title", "task"]
        widgets = {
            "title": TextInput(attrs={
                                'class': 'form-control',
                                'placeholder': 'Название вакансии'
            }),
            "task": Textarea(attrs={
                                'class': 'form-control',
                                'placeholder': 'Описание рабочих обязанностей'
            })
        }