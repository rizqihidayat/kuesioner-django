# Generated by Django 4.1.7 on 2023-05-13 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kuesioner', '0021_userdetail'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetail',
            name='profile_picture',
            field=models.ImageField(blank=True, upload_to='profile_pictures/'),
        ),
    ]
