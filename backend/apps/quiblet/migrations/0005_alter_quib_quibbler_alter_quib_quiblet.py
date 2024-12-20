# Generated by Django 5.1.3 on 2024-12-02 12:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiblet', '0004_quib'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quib',
            name='quibbler',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='quibbled_quibs',
                to='user.profile',
                verbose_name='quibbler',
            ),
        ),
        migrations.AlterField(
            model_name='quib',
            name='quiblet',
            field=models.ForeignKey(
                blank=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name='quibs',
                to='quiblet.quiblet',
                verbose_name='quibs',
            ),
        ),
    ]
