# Generated by Django 3.0.6 on 2020-06-09 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0016_auto_20200609_2023'),
    ]

    operations = [
        migrations.RenameField(
            model_name='story',
            old_name='img',
            new_name='Image',
        ),
        migrations.RenameField(
            model_name='story',
            old_name='filee',
            new_name='Video',
        ),
    ]
