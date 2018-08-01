# Generated by Django 2.0.6 on 2018-07-03 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel_randomizer_app', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Lastgroup',
        ),
        migrations.AlterField(
            model_name='participant',
            name='device_participant',
            field=models.CharField(choices=[('DESKTOP', 'desktop'), ('TABLET', 'tablet'), ('MOBILE', 'mobile')], max_length=7),
        ),
    ]
