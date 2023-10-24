from django.shortcuts import render
from django.views.generic import DetailView, ListView

# Create your views here.
from program.models import Level, Lesson, Subject


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
        'lessons': lessons
    }
    return render(request, 'program/lesson_list.html', context)