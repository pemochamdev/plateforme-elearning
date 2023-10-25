from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView, 
    DeleteView, 
    DetailView, 
    ListView, 
    UpdateView
)

# Create your views here.
from program.models import Level, Lesson, Subject
from program.forms import LessonForm


class LevelListView(ListView):
    model = Level
    template_name = "program/level_list.html"


class SubjectDetailView(DetailView):
    model = Level
    template_name = "program/subject_list.html"



class LessonDetailView(DetailView):
    context_object_name='lesson'
    model = Lesson
    template_name = "program/lesson_detail.html"


def lesson_list(request, slug, niveau):
    level = Level.objects.get(slug=niveau)
    subject = Subject.objects.get(slug=slug)
    lessons  = Lesson.objects.filter(subject=subject).order_by('position')
    context = {
        'lessons': lessons,
        'subject': subject,
        'level': level
    }
    return render(request, 'program/lesson_list.html', context)


class LessonCreateView(CreateView):
    form_class = LessonForm
    context_object_name = 'subject'
    model = Subject
    template_name = "program/lesson_create.html"


    def get_success_url(self):
       self.object = self.get_object()
       level = self.object.level.slug
       
       return reverse_lazy(
           'lesson_list', 
           kwargs={'niveau':level, 'slug': self.object.slug}
        )

    def form_valid(self, form, *args, **kwargs):
        self.object = self.get_object()
        lesson = form.save(commit=False)
        lesson.created_by = self.request.user
        lesson.level = self.object.level
        lesson.subject = self.object
        lesson.save()
        return HttpResponseRedirect(self.get_success_url())
        
    
class LessonUpdateView(UpdateView):
    model = Lesson
    fields = ( 'position', 'name', 'video','fichier_pdf', 'fiche_presentation')
    context_object_name = 'lesson'
    template_name = "program/lesson_update.html"


class LessonDeleteView(DeleteView):
    model = Lesson
    context_object_name = 'lesson'
    template_name = "program/lesson_delete.html"


    def get_success_url(self):
       self.object = self.get_object()
       level = self.object.level.slug
       subject = self.object.subject.slug
       return reverse_lazy(
           'lesson_list', 
           kwargs={'niveau':level, 'slug': subject }
        )
