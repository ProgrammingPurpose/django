# Generated by Django 3.0.3 on 2020-09-05 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_api', '0014_auto_20200905_1331'),
    ]

    operations = [
        migrations.AddField(
            model_name='less_img',
            name='imna',
            field=models.CharField(max_length=10, null=True),
        ),
    ]