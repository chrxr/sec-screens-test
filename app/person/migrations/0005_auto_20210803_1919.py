# Generated by Django 3.1.5 on 2021-08-03 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0004_auto_20210803_1915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rollup',
            name='location',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='rollup',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
