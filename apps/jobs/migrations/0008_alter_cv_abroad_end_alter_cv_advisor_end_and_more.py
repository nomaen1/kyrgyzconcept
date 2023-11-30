# Generated by Django 4.2.6 on 2023-11-29 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0007_alter_cv_abroad_end_alter_cv_advisor_end_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cv',
            name='abroad_end',
            field=models.DateField(blank=True, null=True, verbose_name='Дата окончания'),
        ),
        migrations.AlterField(
            model_name='cv',
            name='advisor_end',
            field=models.DateField(blank=True, null=True, verbose_name='Дата окончания'),
        ),
        migrations.AlterField(
            model_name='cv',
            name='job_title_duty',
            field=models.CharField(max_length=100, verbose_name='Должностные обязанности'),
        ),
        migrations.AlterField(
            model_name='cv',
            name='last_job_end',
            field=models.DateField(blank=True, null=True, verbose_name='Дата окончания'),
        ),
    ]
