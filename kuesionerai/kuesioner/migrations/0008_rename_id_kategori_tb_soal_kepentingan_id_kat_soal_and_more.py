# Generated by Django 4.1.7 on 2023-04-15 05:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kuesioner', '0007_tb_answer_tb_kategori_soal_tb_test_kategori_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tb_soal_kepentingan',
            old_name='id_kategori',
            new_name='id_kat_soal',
        ),
        migrations.RenameField(
            model_name='tb_soal_kepuasan',
            old_name='id_kategori',
            new_name='id_kat_soal',
        ),
    ]
