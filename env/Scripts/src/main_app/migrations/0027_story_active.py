# Generated by Django 3.0.6 on 2020-06-17 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0026_auto_20200617_1557'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
