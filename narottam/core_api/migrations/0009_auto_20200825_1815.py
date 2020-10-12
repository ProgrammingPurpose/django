# Generated by Django 3.0.3 on 2020-08-25 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_api', '0008_audbystu_imagebystu_pdfbystu'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='aud_attachedByStu',
            field=models.ManyToManyField(blank=True, default=None, to='core_api.audByStu'),
        ),
        migrations.AddField(
            model_name='student',
            name='imgAttachedByStu',
            field=models.ManyToManyField(blank=True, default=None, to='core_api.imageByStu'),
        ),
        migrations.AddField(
            model_name='student',
            name='pdf_attachedByStu',
            field=models.ManyToManyField(blank=True, default=None, to='core_api.pdfByStu'),
        ),
    ]