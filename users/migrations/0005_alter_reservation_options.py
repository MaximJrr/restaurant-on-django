# Generated by Django 4.2.1 on 2023-05-18 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_reservation'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reservation',
            options={'verbose_name': 'Бронирование', 'verbose_name_plural': 'Бронирование'},
        ),
    ]