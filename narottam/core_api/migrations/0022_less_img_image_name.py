# Generated by Django 2.1 on 2020-09-14 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_api', '0021_class'),
    ]

    operations = [
        migrations.AddField(
            model_name='less_img',
            name='image_name',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
