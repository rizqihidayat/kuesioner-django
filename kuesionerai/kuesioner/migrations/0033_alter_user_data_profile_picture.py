# Generated by Django 4.1.7 on 2023-05-21 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kuesioner', '0032_user_data_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_data',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='kuesioner/assets/img/illustrations/profile_pictures/'),
        ),
    ]
