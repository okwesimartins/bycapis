# Generated by Django 3.2.3 on 2021-06-13 23:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='use',
            new_name='user',
        ),
    ]
