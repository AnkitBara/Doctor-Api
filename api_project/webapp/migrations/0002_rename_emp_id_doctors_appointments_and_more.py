# Generated by Django 4.1.3 on 2022-11-21 06:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctors',
            old_name='emp_id',
            new_name='appointments',
        ),
        migrations.RenameField(
            model_name='doctors',
            old_name='firstname',
            new_name='dr_name',
        ),
        migrations.RenameField(
            model_name='doctors',
            old_name='lastname',
            new_name='specialist',
        ),
    ]
