# Generated by Django 4.1.7 on 2023-06-16 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kuesioner', '0042_gender_user_data_gender'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Gender',
            new_name='m_gender',
        ),
    ]