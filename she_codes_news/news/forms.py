from django import forms
from django.forms import ModelForm
from .models import NewsStory
from .models import AddComment

class StoryForm(ModelForm):
    # ModelForm from django gives us something from dango 
    class Meta:
        model = NewsStory
        fields = ['title', 'pub_date', 'image', 'content']
        widgets = {
            'pub_date': forms.DateTimeInput(
                format='%d/%m/%Y %H:%M',
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Select a date',
                    'type': 'datetime-local'
                }
            ),
        }


class AddComment(ModelForm):
    class Meta:
        model = AddComment
        fields = ['content']
    

       
            
        