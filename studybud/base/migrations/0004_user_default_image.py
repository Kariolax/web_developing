# Generated by Django 4.0.3 on 2022-03-30 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_user_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='default_image',
            field=models.ImageField(default='avatar.svg', null=True, upload_to=''),
        ),
    ]
