# Generated by Django 4.1.7 on 2023-05-13 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kuesioner', '0026_userdetail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdetail',
            name='email',
        ),
        migrations.RemoveField(
            model_name='userdetail',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='userdetail',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='userdetail',
            name='username',
        ),
    ]