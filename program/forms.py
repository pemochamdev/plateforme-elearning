from django import forms
from django import forms
from django.db.migrations.state import get_related_models_tuples
from .models import Comment
from django.utils.translation import gettext_lazy as _


from program.models import (
    Comment,
    Lesson, 
    Level,
    Response,
    Subject, 
)

class LessonForm(forms.ModelForm):
    
    class Meta:
        model = Lesson
        fields = ( 'position', 'name', 'video','fichier_pdf', 'fiche_presentation')



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        

        fields = ['content','parent']
        
        labels = {
            'content': _(''),
        }
        
        widgets = {
            'content' : forms.TextInput(),
        }

class ResponseForm(forms.ModelForm):
    
    class Meta:
        model = Response
        fields = ("content",)
        labels = {'content': 'Reponses'}
        widgets = {
            'content':forms.Textarea(attrs={
                'class':'form-control',
                'rows':3,
                'cols':40,
                'placeholder':'Repondez a ce commentaire ici.'
            })
        }  
