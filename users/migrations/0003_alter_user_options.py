# Generated by Django 4.2 on 2024-08-03 19:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_rename_token_user_code'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'permissions': [('can_deactivate_user', 'Can deactivate user')], 'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
    ]
