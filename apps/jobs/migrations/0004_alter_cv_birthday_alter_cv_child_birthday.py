# Generated by Django 4.2.6 on 2023-12-05 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_cv_edu_end_alter_cv_edu_start'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cv',
            name='birthday',
            field=models.DateField(verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='cv',
            name='child_birthday',
            field=models.DateField(blank=True, null=True, verbose_name='День рождение'),
        ),
    ]
