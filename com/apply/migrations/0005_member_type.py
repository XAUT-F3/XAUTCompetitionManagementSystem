# Generated by Django 2.2.10 on 2021-08-27 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apply', '0004_auto_20210824_1246'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='type',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]