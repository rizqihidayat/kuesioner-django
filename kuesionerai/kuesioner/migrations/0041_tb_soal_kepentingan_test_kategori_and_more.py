# Generated by Django 4.1.7 on 2023-06-08 16:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kuesioner', '0040_userresponse2'),
    ]

    operations = [
        migrations.AddField(
            model_name='tb_soal_kepentingan',
            name='test_kategori',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='kuesioner.tb_test_kategori'),
        ),
        migrations.AddField(
            model_name='tb_soal_kepuasan',
            name='test_kategori',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='kuesioner.tb_test_kategori'),
        ),
    ]
