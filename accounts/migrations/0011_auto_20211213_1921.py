# Generated by Django 3.2.9 on 2021-12-13 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20211209_2124'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='phone_number',
            new_name='phone_num',
        ),
        migrations.AddField(
            model_name='profile',
            name='age',
            field=models.IntegerField(default='0'),
        ),
    ]