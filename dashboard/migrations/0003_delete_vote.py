# Generated by Django 3.2.5 on 2021-11-20 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_vote'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Vote',
        ),
    ]