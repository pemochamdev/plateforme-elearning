################ Author: https://github.com/pemochamdev #####################

from django.db import models
from django.urls import reverse
from django.utils.html import mark_safe
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
import uuid

# Create your models here.

def user_directory_path(instance, files):
    return 'user_{0}/{1}'.format(instance.user.username, files)



class Level(models.Model):
    name = models.CharField(
        max_length=100
    )
    slug = models.SlugField(blank=True, null=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Subject(models.Model):
    uuid = models.UUIDField(
        unique=True, 
        editable=False,
        default = uuid.uuid4,
        max_length=10
    )
    name = models.CharField(
        max_length=100
    )
    slug = models.SlugField()
    level = models.ForeignKey(
        Level,
        on_delete=models.CASCADE, 
        related_name='level_subject'
    )
    picture = models.ImageField(
        upload_to="SUBJECTS"
    )
    description = models.TextField(
        max_length=500
    )

    def __str__(self):
        return self.name

    
    def get_image_subject(self):
        return mark_safe('<img src="%s" with="50" height="50" />' % (self.picture.url))



class Lesson(models.Model):
    uuid = models.UUIDField(
        unique=True, 
        editable=False, 
        default = uuid.uuid4,
        max_length=10
        )
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    position = models.PositiveSmallIntegerField(
        verbose_name='CHAPTER '
    )
 
    level = models.ForeignKey(
        Level, 
        on_delete=models.CASCADE, 
        related_name='level_lesson'
    )
    created_by = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name='author'
    )
    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        related_name='lesson'
    )
    video = models.FileField(
        upload_to="VIDEO",
        blank=True, 
        null=True ,
        verbose_name="VIDEO"
    )
    fichier_pdf = models.FileField(
        upload_to="FICHE_PDF", 
        blank=True, 
        null=True, 
        verbose_name="FICHE_PDF"
    )
    fiche_presentation = models.FileField(
        upload_to="FICHE_PRESENTATION", 
        blank=True, 
        null=True, 
        verbose_name="FICHE_PRESENTATION"
    )

    class Meta:
        ordering = ['-position']
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("lesson_list", kwargs={"slug": self.subject.slug, 'niveau': self.level.slug})
    
    
    
    def get_file_type(self, file_field):
        
        #Recuperation du nom de fichier
        file_name = getattr(self, file_field).name

        #Extraire l'extension du fichier
        file_extension = file_name.split('.')[-1].lower()

        #determiner le type du  fichier en fonction de l'extension
        if file_extension in [
            'mp4','avi', 'mkv', 'mov', 'wmv'
            ]:

            return 'VIDEO'
        
        elif file_extension in ['pptx', 'ppt', 'txt', 'doc']:
            return 'FICHIER DE PRESENTATION'
        
        elif file_extension == 'pdf':
            return 'PDF'
        
        else:
            return 'Fichier non pris en charge'

    
    def get_video_type(self):
        return self.get_file_type('video')
    

    def get_pdf_type(self):
        return self.get_file_type('fichier_pdf')
     
    def get_prsentation_type(self):
        return self.get_file_type('fiche_presentation')
    




    