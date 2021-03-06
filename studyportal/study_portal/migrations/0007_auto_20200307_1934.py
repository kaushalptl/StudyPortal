# Generated by Django 3.0.1 on 2020-03-07 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study_portal', '0006_auto_20200227_2248'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tutorial',
            fields=[
                ('tut_id', models.AutoField(primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=50)),
                ('topic_name', models.CharField(max_length=100)),
                ('sq_no', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='course',
            name='sq_no',
        ),
        migrations.RemoveField(
            model_name='course',
            name='topic_name',
        ),
        migrations.RemoveField(
            model_name='material',
            name='course_id',
        ),
        migrations.AlterField(
            model_name='course',
            name='course_name',
            field=models.CharField(max_length=100),
        ),
    ]
