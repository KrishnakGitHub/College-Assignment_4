# Generated by Django 3.2.5 on 2021-08-18 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_student_student_department'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lecturer',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['name']},
        ),
        migrations.RenameField(
            model_name='lecturer',
            old_name='Lecturer_Department',
            new_name='Department',
        ),
        migrations.RenameField(
            model_name='lecturer',
            old_name='Lecturer_Name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='Student_Department',
            new_name='Department',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='Student_Name',
            new_name='name',
        ),
    ]
