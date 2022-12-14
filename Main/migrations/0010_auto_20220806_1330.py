# Generated by Django 3.2.9 on 2022-08-06 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0009_auto_20220727_1323'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='airlines',
            name='date',
        ),
        migrations.RemoveField(
            model_name='flight_book',
            name='flight',
        ),
        migrations.AddField(
            model_name='airlines',
            name='available',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='airlines',
            name='flying_date',
            field=models.CharField(default='08/01/2022', max_length=50),
        ),
        migrations.AddField(
            model_name='airlines',
            name='total_seats',
            field=models.PositiveIntegerField(default=100),
        ),
    ]
