# Generated by Django 2.0.6 on 2018-06-20 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lastgroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('survey_code', models.IntegerField()),
                ('last_group', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Participants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentnumber_enc', models.TextField()),
                ('url', models.CharField(max_length=250)),
                ('participation_date', models.DateTimeField(verbose_name='participation date')),
                ('device_participant', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Surveys',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('survey_code', models.IntegerField()),
                ('survey_name', models.CharField(max_length=200)),
                ('number_of_goups', models.IntegerField()),
                ('question_name_student_enc', models.CharField(max_length=200)),
            ],
        ),
    ]
