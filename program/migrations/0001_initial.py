# Generated by Django 4.2.6 on 2023-10-23 11:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import program.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(editable=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('picture', models.ImageField(upload_to=program.models.user_directory_path)),
                ('description', models.TextField(max_length=500)),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='level_subject', to='program.level')),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(editable=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('position', models.PositiveSmallIntegerField(verbose_name='CHAPTER ')),
                ('video', models.FileField(blank=True, null=True, upload_to=program.models.user_directory_path, verbose_name='VIDEO')),
                ('fichier_pdf', models.FileField(blank=True, null=True, upload_to=program.models.user_directory_path, verbose_name='FICHE_PDF')),
                ('fiche_presentation', models.FileField(blank=True, null=True, upload_to=program.models.user_directory_path, verbose_name='FICHE_PRESENTATION')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL)),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='level_lesson', to='program.level')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subj_lesson', to='program.subject')),
            ],
            options={
                'ordering': ['-position'],
            },
        ),
    ]
