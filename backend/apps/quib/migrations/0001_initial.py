# Generated by Django 5.1.3 on 2024-12-07 04:12

import django.db.models.deletion
import shortuuid.django_fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('quiblet', '0003_delete_quib'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quib',
            fields=[
                (
                    'created_at',
                    models.DateTimeField(auto_now_add=True, verbose_name='create at'),
                ),
                ('is_public', models.BooleanField(default=True, verbose_name='is public')),
                (
                    'id',
                    shortuuid.django_fields.ShortUUIDField(
                        alphabet='abcdefghijklmnopqrstuvwxyz0123456789',
                        editable=False,
                        length=7,
                        max_length=7,
                        prefix='',
                        primary_key=True,
                        serialize=False,
                        verbose_name='id',
                    ),
                ),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                (
                    'slug',
                    models.SlugField(
                        blank=True, editable=False, max_length=25, verbose_name='slug'
                    ),
                ),
                ('content', models.TextField(verbose_name='content')),
                (
                    'dislikes',
                    models.ManyToManyField(
                        blank=True,
                        related_name='disliked_quibs',
                        to='user.profile',
                        verbose_name='dislikes',
                    ),
                ),
                (
                    'likes',
                    models.ManyToManyField(
                        blank=True,
                        related_name='liked_quibs',
                        to='user.profile',
                        verbose_name='likes',
                    ),
                ),
                (
                    'quibber',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='quibs',
                        to='user.profile',
                        verbose_name='quibber',
                    ),
                ),
                (
                    'quiblet',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='quibs',
                        to='quiblet.quiblet',
                        verbose_name='quiblet',
                    ),
                ),
            ],
            options={
                'verbose_name': 'Quib',
                'verbose_name_plural': 'Quibs',
                'ordering': ['-created_at'],
            },
        ),
    ]
