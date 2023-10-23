################ Author: https://github.com/pemochamdev #####################

from django.db import models
from django.contrib.auth.models import User
from django.utils.html import mark_safe
from django.db.models.signals import post_save




# Create your models here.

def user_directory_path(instance , filename):
    return "user_{0}/{1}".format(instance.user.username, filename)


USER_CHOICES = (
    ('et', 'Etudiant'),
    ('pa', 'Parent'),
    ('en', 'Enseignant')
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    profile_type = models.CharField(max_length=2, choices=USER_CHOICES)
    profile_picture = models.ImageField(upload_to=user_directory_path, default='profile.png')
    profile_info = models.TextField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    # favorites = models.ManyToManyField(Post)

    def __str__(self):
        return self.user.username

    def profile_image(self):
        return mark_safe('<img src="%s" with="50" height="50" />' % (self.profile_picture.url))

    

def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
	instance.profile.save()

post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)
