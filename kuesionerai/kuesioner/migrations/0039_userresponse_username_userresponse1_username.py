# Generated by Django 4.1.7 on 2023-06-07 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kuesioner', '0038_userresponse_score_userresponse1_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='userresponse',
            name='username',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='userresponse1',
            name='username',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]