# Generated by Django 3.2.18 on 2023-03-27 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kuesioner', '0004_alter_tb_master_answer_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tb_master_kategori_soal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_kategori', models.IntegerField(blank=True, default=None, null=True)),
                ('kategori_soal', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
            ],
            options={
                'db_table': 'Tb_master_kategori_soal',
            },
        ),
        migrations.CreateModel(
            name='Tb_soal_kepentingan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_kategori', models.IntegerField(blank=True, default=None, null=True)),
                ('id_master_answer', models.IntegerField(blank=True, default=None, null=True)),
                ('pertanyaan', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
            ],
            options={
                'db_table': 'Tb_soal_kepentingan',
            },
        ),
        migrations.CreateModel(
            name='Tb_soal_kepuasan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_kategori', models.IntegerField(blank=True, default=None, null=True)),
                ('id_master_answer', models.IntegerField(blank=True, default=None, null=True)),
                ('pertanyaan', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
            ],
            options={
                'db_table': 'Tb_soal_kepuasan',
            },
        ),
        migrations.CreateModel(
            name='Tb_soal_kepuasan_umum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_master_answer', models.IntegerField(blank=True, default=None, null=True)),
                ('pertanyaan', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
            ],
            options={
                'db_table': 'Tb_soal_kepuasan_umum',
            },
        ),
        migrations.AlterField(
            model_name='tb_master_answer',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='tb_master_kategori_answer',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date published'),
        ),
        migrations.AlterModelTable(
            name='tb_master_answer',
            table='Tb_master_answer',
        ),
        migrations.AlterModelTable(
            name='tb_master_kategori_answer',
            table='Tb_master_kategori_answer',
        ),
    ]