# Generated by Django 4.1.7 on 2023-05-13 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kuesioner', '0023_remove_userdetail_user_userdetail_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdetail',
            name='email',
        ),
        migrations.RemoveField(
            model_name='userdetail',
            name='username',
        ),
    ]
