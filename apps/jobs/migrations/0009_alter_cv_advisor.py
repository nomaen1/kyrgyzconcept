# Generated by Django 4.2.6 on 2023-11-29 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0008_alter_cv_abroad_end_alter_cv_advisor_end_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cv',
            name='advisor',
            field=models.CharField(max_length=100, null=True, verbose_name='ФИО'),
        ),
    ]