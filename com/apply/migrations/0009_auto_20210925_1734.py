# Generated by Django 2.2.10 on 2021-09-25 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apply', '0008_auto_20210831_1942'),
    ]

    operations = [
        migrations.RenameField(
            model_name='race_message',
            old_name='m_signup_requset',
            new_name='m_signup_request',
        ),
    ]
