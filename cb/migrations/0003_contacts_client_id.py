# Generated by Django 4.2.11 on 2024-05-07 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cb', '0002_remove_contacts_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacts',
            name='client_id',
            field=models.CharField(default='', max_length=100),
        ),
    ]
