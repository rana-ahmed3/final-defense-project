# Generated by Django 3.1.1 on 2020-10-02 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Feedback', '0002_contact_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='phone',
        ),
    ]
