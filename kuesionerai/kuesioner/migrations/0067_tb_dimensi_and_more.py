from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kuesioner', '0066_rename_kat_soal_tb_soal_kepentingan_dimensi_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='tb_dimensi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kat_dimensi', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
            ],
            options={
                'db_table': 'tb_dimensi',
            },
        ),
        migrations.RenameField(
            model_name='tb_kategori_soal',
            old_name='kat_dimensi',
            new_name='kat_lvl_kepuasan',
        ),
        migrations.RenameField(
            model_name='tb_soal_kepentingan',
            old_name='dimensi',
            new_name='lvl_kepuasan',
        ),
        migrations.RenameField(
            model_name='tb_soal_kepuasan',
            old_name='dimensi',
            new_name='lvl_kepuasan',
        ),
        migrations.RenameField(
            model_name='userresponse1',
            old_name='kat_soal',
            new_name='lvl_kepuasan',
        ),
        migrations.RenameField(
            model_name='userresponse2',
            old_name='kat_soal',
            new_name='lvl_kepuasan',
        ),
        migrations.RemoveField(
            model_name='count_user_umum',
            name='total_score',
        ),
        migrations.AlterField(
            model_name='count_user_umum',
            name='user_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterModelTable(
            name='count_user_umum',
            table=None,
        ),
        migrations.CreateModel(
            name='score_lvl_kepuasan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_score', models.IntegerField(default=0)),
                ('lvl_kepuasan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kuesioner.tb_kategori_soal')),
                ('test_kategori', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='kuesioner.tb_test_kategori')),
            ],
            options={
                'db_table': 'tb_score_lvl_kepuasan',
            },
        ),
        migrations.CreateModel(
            name='score_lvl_kepentingan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_score', models.IntegerField(default=0)),
                ('lvl_kepuasan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kuesioner.tb_kategori_soal')),
                ('test_kategori', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='kuesioner.tb_test_kategori')),
            ],
            options={
                'db_table': 'tb_score_lvl_kepentingan',
            },
        ),
        migrations.CreateModel(
            name='score_dimensi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_id', models.IntegerField()),
                ('score_difference', models.IntegerField()),
                ('average_score_difference', models.FloatField(blank=True, null=True)),
                ('dimensi', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='kuesioner.tb_dimensi')),
            ],
            options={
                'db_table': 'tb_score_dimensi',
            },
        ),
        migrations.CreateModel(
            name='dimensi_kepuasan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('total_score', models.IntegerField(default=0)),
                ('dimensi', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='kuesioner.tb_dimensi')),
                ('question', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='kuesioner.tb_soal_kepuasan')),
                ('test', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='kuesioner.tb_test_kategori')),
            ],
            options={
                'db_table': 'tb_dimensi_kepuasan',
                'unique_together': {('test', 'dimensi', 'question')},
            },
        ),
        migrations.CreateModel(
            name='dimensi_kepentingan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('total_score', models.IntegerField(default=0)),
                ('dimensi', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='kuesioner.tb_dimensi')),
                ('question', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='kuesioner.tb_soal_kepentingan')),
                ('test', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='kuesioner.tb_test_kategori')),
            ],
            options={
                'db_table': 'tb_dimensi_kepentingan',
                'unique_together': {('test', 'dimensi', 'question')},
            },
        ),
    ]
