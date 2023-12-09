# Generated by Django 4.2.6 on 2023-12-08 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0013_remove_cv_laptop'),
    ]

    operations = [
        migrations.AddField(
            model_name='cv',
            name='google_docs',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Google Документы'),
        ),
        migrations.AddField(
            model_name='cv',
            name='google_presentation',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Google Презентации'),
        ),
        migrations.AddField(
            model_name='cv',
            name='google_tables',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Google Таблицы'),
        ),
        migrations.AddField(
            model_name='cv',
            name='laptop',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Имеется ли у Вас ноутбук?'),
        ),
        migrations.AddField(
            model_name='cv',
            name='prezi',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Prezi'),
        ),
        migrations.AddField(
            model_name='cv',
            name='touch_typing',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Слепая печать'),
        ),
    ]