# Generated by Django 3.0.1 on 2020-03-11 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('study_portal', '0010_auto_20200309_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='answer',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='answer',
            name='course_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='study_portal.Course'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question',
            field=models.CharField(default='', max_length=255),
        ),
    ]
