from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView, 
    DeleteView, 
    DetailView,
    FormView, 
    ListView, 
    UpdateView,
)

# Create your views here.
from program.models import Level, Lesson, Subject, Comment
from program.forms import LessonForm,CommentForm,ResponseForm



class LevelListView(ListView):
    context_object_name = 'levels'
    model = Level
    template_name = "program/level_list.html"


def level_list(request):
    template_name = "program/level_list.html"

    levels = Level.objects.all()
    context = {
        'levels': levels
    }
    return render(request, template_name, context)



class SubjectDetailView(DetailView):
    model = Level
    template_name = "program/subject_list.html"
 

class LessonDetailView(DetailView):
    template_name = 'program/lesson_detail.html'

    model= Lesson

    def get_context_data(self , **kwargs):
        data = super().get_context_data(**kwargs)
        connected_comments = Comment.objects.filter(CommentLesson=self.get_object())
        number_of_comments = connected_comments.count()
        data['comments'] = connected_comments
        data['no_of_comments'] = number_of_comments
        data['comment_form'] = CommentForm()
        return data

    def post(self , request , *args , **kwargs):
        if self.request.method == 'POST':
            print('-------------------------------------------------------------------------------Reached here')
            comment_form = CommentForm(self.request.POST)
            if comment_form.is_valid():
                content = comment_form.cleaned_data['content']
                try:
                    parent = comment_form.cleaned_data['parent']
                except:
                    parent=None

            

            new_comment = Comment(content=content , author = self.request.user , CommentLesson=self.get_object() , parent=parent)
            new_comment.save()
            return redirect(self.request.path_info)
                     





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

