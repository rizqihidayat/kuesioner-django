# Generated by Django 4.2.3 on 2023-07-22 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kuesioner', '0071_rename_total_score_lvl_kepuasan_tb_score_lvl_total_score_lvl_kepuasans'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tb_score_lvl',
            name='total_score_lvl_kepuasans',
        ),
    ]
