# Generated by Django 2.2.10 on 2021-08-19 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apply', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='T_remark',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='T_slogan',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
