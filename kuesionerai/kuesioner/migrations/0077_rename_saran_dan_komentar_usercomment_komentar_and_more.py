# Generated by Django 4.2.3 on 2023-07-28 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kuesioner', '0076_usercomment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usercomment',
            old_name='saran_dan_komentar',
            new_name='komentar',
        ),
        migrations.AddField(
            model_name='usercomment',
            name='saran',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]