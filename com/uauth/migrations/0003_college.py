# Generated by Django 2.2.10 on 2021-10-15 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uauth', '0002_auto_20210828_1254'),
    ]

    operations = [
        migrations.CreateModel(
            name='college',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college_name', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'college',
            },
        ),
    ]