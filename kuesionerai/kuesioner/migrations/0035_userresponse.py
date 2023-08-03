# Generated by Django 4.1.7 on 2023-05-30 14:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('kuesioner', '0034_alter_user_data_profile_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kuesioner.tb_answer')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kuesioner.tb_soal_kepuasan_umum')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'UserResponse',
            },
        ),
    ]