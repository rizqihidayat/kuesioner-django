# Generated by Django 4.1.7 on 2023-05-13 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kuesioner', '0019_m_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='m_position',
            name='position',
            field=models.TextField(),
        ),
    ]
