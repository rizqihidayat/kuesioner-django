# Generated by Django 4.1.7 on 2023-07-03 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kuesioner', '0052_alter_count_user_umum_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='count_user_umum',
            name='total_score',
            field=models.IntegerField(default=0),
        ),
    ]