# Generated by Django 4.1.7 on 2023-05-13 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kuesioner', '0016_delete_userprofileinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='m_location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
            ],
            options={
                'db_table': 'm_location',
            },
        ),
        migrations.CreateModel(
            name='m_position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
            ],
            options={
                'db_table': 'm_position',
            },
        ),
    ]
