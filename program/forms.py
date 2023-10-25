from django import forms

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
        fields = ("content",)
        widget = {
            'content': forms.Textarea(attrs={
                'placeholder':'add your comment here',
                'rows':4,
                'cols':70
            })
        }


class ResponseForm(forms.ModelForm):
    
    class Meta:
        model = Response
        fields = ("content",)
        widget = {
            'content': forms.Textarea(attrs={
                'placeholder':'add your response here',
                'rows':3,
                'cols':50
            })
        }
