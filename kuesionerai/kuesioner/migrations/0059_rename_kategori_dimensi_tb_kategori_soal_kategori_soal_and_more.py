# Generated by Django 4.2.3 on 2023-07-15 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kuesioner', '0058_rename_kat_tb_soal_kepentingan_kat_soal'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tb_kategori_soal',
            old_name='kategori_dimensi',
            new_name='kategori_soal',
        ),
        migrations.RenameField(
            model_name='tb_kategori_soal',
            old_name='test',
            new_name='test_kategori',
        ),
    ]
