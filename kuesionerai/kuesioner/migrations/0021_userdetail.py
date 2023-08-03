# Generated by Django 4.1.7 on 2023-05-13 11:55

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
            name='UserDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=20)),
                ('birthday', models.DateField()),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kuesioner.m_location')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kuesioner.m_position')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'm_user_detail',
            },
        ),
    ]