# Generated by Django 2.2 on 2019-08-11 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsweb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mondaq',
            name='create_date',
            field=models.CharField(max_length=255, verbose_name='时间'),
        ),
    ]
