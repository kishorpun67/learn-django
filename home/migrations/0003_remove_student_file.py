# Generated by Django 4.2.7 on 2023-11-21 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_student_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='file',
        ),
    ]
