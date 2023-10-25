from django.urls import path

from program import views

urlpatterns = [
    
    path(
        'level-list/', 
        views.LevelListView.as_view(), 
        name='level_list'
    ),
    
    path(
        '<slug>/', 
        views.SubjectDetailView.as_view(), 
        name='subject_list'
    ),
    
    path(
        '<str:niveau>/<slug>/', 
        views.lesson_list, 
        name='lesson_list'
    ),
    
    path(
        '<str:niveau>/<str:slug>/create', 
        views.LessonCreateView.as_view(), 
        name='lesson_create'
    ),
    
    path(
        '<str:niveau>/<str:subject>/<slug>/', 
        views.LessonDetailView.as_view(), 
        name='lesson_detail'
    ),
    
    path(
        '<str:niveau>/<str:subject>/<slug>/update/', 
        views.LessonUpdateView.as_view(), 
        name='lesson_update'
    ),
    
    path(
        '<str:niveau>/<str:subject>/<slug>/delete/', 
        views.LessonDeleteView.as_view(), 
        name='lesson_delete'
    ),
]
