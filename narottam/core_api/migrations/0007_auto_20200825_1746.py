# Generated by Django 3.0.3 on 2020-08-25 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core_api', '0006_auto_20200821_2112'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='aud_stu',
        ),
        migrations.RemoveField(
            model_name='student',
            name='image_stu',
        ),
        migrations.RemoveField(
            model_name='student',
            name='pdf_stu',
        ),
    ]