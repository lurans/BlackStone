# Generated by Django 3.1.5 on 2021-01-18 08:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_auto_20210117_2311'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topicname',
            old_name='image_description',
            new_name='topic_description',
        ),
        migrations.RenameField(
            model_name='topicname',
            old_name='image_name',
            new_name='topic_name',
        ),
    ]
