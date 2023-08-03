# Generated by Django 4.1.7 on 2023-05-13 13:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('kuesioner', '0025_delete_userdetail'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=255)),
                ('phone', models.CharField(max_length=20)),
                ('birthday', models.DateField()),
                ('profile_picture', models.ImageField(blank=True, upload_to='profile_pictures/')),
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
