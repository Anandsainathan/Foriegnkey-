# Generated by Django 4.2.5 on 2023-09-29 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courseapp', '0003_rename_course_student_course'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='Course',
            new_name='course_name',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='Fee',
            new_name='fee',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='Address',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='Age',
            new_name='age',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='Date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='Name',
            new_name='name',
        ),
    ]
