# Generated by Django 3.0.7 on 2020-12-15 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teas', '0002_auto_20200624_1925'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tea',
            old_name='description',
            new_name='comment',
        ),
        migrations.RemoveField(
            model_name='tea',
            name='form',
        ),
    ]
