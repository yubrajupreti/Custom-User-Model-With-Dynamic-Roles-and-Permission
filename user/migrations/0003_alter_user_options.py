# Generated by Django 3.2.10 on 2021-12-26 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_is_staff'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'permissions': [('create_user', 'Can create a user'), ('list_user', 'Can list all the user'), ('update_user', 'Can update detail of all user'), ('delete_users', 'Can delete any user')]},
        ),
    ]
