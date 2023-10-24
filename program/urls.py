from django.urls import path

from program import views

urlpatterns = [
    
    path('level-list/', views.LevelListView.as_view(), name='level_list'),
    
    path('<slug>/', views.SubjectDetailView.as_view(), name='subject_list'),
    
    path('<str:niveau>/<slug>/', views.lesson_list, name='lesson_list'),
    
    path(
        '<str:niveau>/<str:subject>/<slug>/', 
        views.LessonDetailView.as_view(), 
        name='lesson_detail'
    ),
]
