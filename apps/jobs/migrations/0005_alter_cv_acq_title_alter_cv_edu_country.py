# Generated by Django 4.2.6 on 2023-12-05 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_alter_cv_birthday_alter_cv_child_birthday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cv',
            name='acq_title',
            field=models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='Должность'),
        ),
        migrations.AlterField(
            model_name='cv',
            name='edu_country',
            field=models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='Страна Университета'),
        ),
    ]
