# Generated by Django 4.0.3 on 2022-03-18 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_rename_describtion_room_description_remove_room_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Room',
            new_name='Entry',
        ),
    ]
