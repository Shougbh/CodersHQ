# Generated by Django 3.0.11 on 2021-02-15 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hackathon', '0008_hackathon_subtile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hackathon',
            old_name='subtile',
            new_name='subtitle',
        ),
    ]
