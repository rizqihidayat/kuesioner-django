# Generated by Django 4.1.7 on 2023-04-15 06:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kuesioner', '0010_rename_id_kat_soal_tb_soal_kepuasan_umum_id_kategori'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tb_soal_kepuasan_umum',
            old_name='id_kategori',
            new_name='test_kategori',
        ),
    ]
