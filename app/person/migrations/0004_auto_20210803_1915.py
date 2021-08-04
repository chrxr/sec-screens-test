# Generated by Django 3.1.5 on 2021-08-03 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0003_rollup'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedperson',
            old_name='fullname',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='fullname',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='place',
            old_name='nonpersonname',
            new_name='name',
        ),
    ]
