# Generated by Django 4.2.11 on 2024-05-07 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cb', '0004_remove_contacts_address_remove_contacts_client_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacts',
            name='address',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='contacts',
            name='client_id',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='contacts',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AddField(
            model_name='contacts',
            name='f_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='contacts',
            name='l_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='contacts',
            name='nickname',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='contacts',
            name='phone',
            field=models.CharField(default='', max_length=100),
        ),
    ]