# Generated by Django 4.2.3 on 2023-07-22 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kuesioner', '0067_tb_dimensi_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TotalScoreLvlKepuasan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_score', models.IntegerField(default=0)),
                ('lvl_kepuasan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kuesioner.tb_kategori_soal')),
            ],
            options={
                'db_table': 'tb_score_lvl',
            },
        ),
    ]
