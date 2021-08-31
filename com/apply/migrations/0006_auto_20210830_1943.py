# Generated by Django 2.2.10 on 2021-08-30 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apply', '0005_member_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Honor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('honor', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='race_name',
            name='end_date',
            field=models.DateTimeField(default='2121-9-1 00:00:00'),
        ),
        migrations.AddField(
            model_name='race_name',
            name='start_date',
            field=models.DateTimeField(default='2021-9-1 00:00:00'),
        ),
    ]