# Generated by Django 3.2.18 on 2023-03-26 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kuesioner', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tb_master_answer',
            name='desc',
            field=models.TextField(default=None),
        ),
    ]
