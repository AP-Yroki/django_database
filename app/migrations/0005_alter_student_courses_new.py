# Generated by Django 4.2.6 on 2023-12-14 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rename_courses_student_courses_new'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='courses_new',
            field=models.ManyToManyField(to='app.course'),
        ),
    ]