# Generated by Django 2.0.6 on 2018-09-27 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('panel_randomizer_app', '0008_survey_language'),
    ]

    operations = [
        migrations.CreateModel(
            name='SurveyGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_number', models.IntegerField(help_text='The group number')),
                ('fill_count', models.PositiveIntegerField(help_text='The number of participants you want in this group')),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='panel_randomizer_app.Survey')),
            ],
        ),
    ]