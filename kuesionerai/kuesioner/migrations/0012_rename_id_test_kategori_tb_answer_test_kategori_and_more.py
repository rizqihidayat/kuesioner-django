# Generated by Django 4.1.7 on 2023-04-15 06:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kuesioner', '0011_rename_id_kategori_tb_soal_kepuasan_umum_test_kategori'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tb_answer',
            old_name='id_test_kategori',
            new_name='test_kategori',
        ),
        migrations.RenameField(
            model_name='tb_kategori_soal',
            old_name='id_kategori',
            new_name='test_kategori',
        ),
        migrations.RenameField(
            model_name='tb_soal_kepentingan',
            old_name='id_kat_soal',
            new_name='kat_soal',
        ),
        migrations.RenameField(
            model_name='tb_soal_kepuasan',
            old_name='id_kat_soal',
            new_name='kat_soal',
        ),
    ]