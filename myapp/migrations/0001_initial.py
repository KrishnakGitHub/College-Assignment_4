# Generated by Django 3.2.5 on 2021-08-18 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Student_Name', models.CharField(max_length=100)),
                ('Student_Department', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.department')),
            ],
            options={
                'ordering': ['Student_Name'],
            },
        ),
        migrations.CreateModel(
            name='Lecturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Lecturer_Name', models.CharField(max_length=100)),
                ('Lecturer_Department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.department')),
            ],
            options={
                'ordering': ['Lecturer_Name'],
            },
        ),
    ]
