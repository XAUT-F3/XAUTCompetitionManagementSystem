# Generated by Django 2.2.10 on 2021-08-24 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0002_auto_20210823_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='type',
            field=models.CharField(max_length=10),
        ),
    ]
