# Generated by Django 2.1 on 2020-09-10 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core_api', '0019_remove_subject_batch_attached'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='class',
            name='lesson_attached',
        ),
        migrations.RemoveField(
            model_name='class',
            name='student_enrolled',
        ),
        migrations.DeleteModel(
            name='Class',
        ),
    ]