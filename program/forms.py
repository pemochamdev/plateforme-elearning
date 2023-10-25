from django import forms

from program.models import Lesson, Subject, Level

class LessonForm(forms.ModelForm):
    
    class Meta:
        model = Lesson
        fields = ( 'position', 'name', 'video','fichier_pdf', 'fiche_presentation')
