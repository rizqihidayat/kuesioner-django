# Generated by Django 4.2.3 on 2023-07-22 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kuesioner', '0072_remove_tb_score_lvl_total_score_lvl_kepuasans'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tb_score_lvl',
            old_name='total_score_lvl_kepentingan',
            new_name='total_score_lvl_kepuasan',
        ),
    ]
