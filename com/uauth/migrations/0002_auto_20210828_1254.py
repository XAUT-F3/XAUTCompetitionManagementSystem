# Generated by Django 2.2.10 on 2021-08-28 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uauth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='s_birthday',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='teachers',
            name='t_birthday',
            field=models.DateField(blank=True, null=True),
        ),
    ]