# Generated by Django 4.1.7 on 2023-05-19 09:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('kuesioner', '0020_alter_m_position_position'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=200)),
                ('birthday', models.DateField(verbose_name='birthday')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('id_auth_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('id_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kuesioner.m_location')),
                ('id_position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kuesioner.m_position')),
            ],
            options={
                'db_table': 'user_data',
            },
        ),
    ]