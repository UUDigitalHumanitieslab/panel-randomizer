# Generated by Django 2.0.6 on 2018-08-28 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel_randomizer_app', '0007_auto_20180821_0935'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='language',
            field=models.CharField(choices=[('nl-NL', 'Dutch'), ('en-GB', 'English')], default='en-GB', max_length=5),
        ),
    ]