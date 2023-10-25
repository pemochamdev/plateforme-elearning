from django.contrib import admin

# Register your models here.

from program.models import (
    Comment,
    Lesson, 
    Level, 
    Subject, 
    Response
)

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'level', 'get_image_subject']
    prepopulated_fields = {"slug": ("name",)}
    

@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'created_at']
    prepopulated_fields = {"slug": ("name",)}



@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['name', 'position','level','created_by', 'subject']
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Response)
admin.site.register(Comment)