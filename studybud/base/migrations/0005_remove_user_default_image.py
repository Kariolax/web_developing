# Generated by Django 4.0.3 on 2022-03-30 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_user_default_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='default_image',
        ),
    ]
