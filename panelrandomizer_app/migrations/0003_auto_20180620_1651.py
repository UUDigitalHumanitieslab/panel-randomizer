# Generated by Django 2.0.6 on 2018-06-20 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panelrandomizer_app', '0002_auto_20180620_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surveys',
            name='survey_code',
            field=models.CharField(max_length=200),
        ),
    ]
