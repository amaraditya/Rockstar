# Generated by Django 3.0.5 on 2020-04-12 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movies',
            name='alias',
        ),
    ]
