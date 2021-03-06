# Generated by Django 3.1.5 on 2021-07-29 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedPerson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eppn', models.CharField(blank=True, max_length=255, null=True, verbose_name='EPPN')),
                ('firstname', models.CharField(blank=True, max_length=255, null=True, verbose_name='First name')),
                ('lastname', models.CharField(blank=True, max_length=255, null=True, verbose_name='Last name')),
                ('location', models.CharField(blank=True, max_length=255, null=True, verbose_name='Location')),
                ('fullname', models.CharField(blank=True, max_length=255, null=True, verbose_name='Full name')),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nonpersonname', models.CharField(blank=True, max_length=255, null=True, verbose_name='First name')),
                ('location', models.CharField(blank=True, max_length=255, null=True, verbose_name='Location')),
            ],
        ),
        migrations.RemoveField(
            model_name='person',
            name='eppn',
        ),
        migrations.RemoveField(
            model_name='person',
            name='firstnameOverride',
        ),
        migrations.RemoveField(
            model_name='person',
            name='fullnameOverride',
        ),
        migrations.RemoveField(
            model_name='person',
            name='lastnameOverride',
        ),
        migrations.RemoveField(
            model_name='person',
            name='locationOverride',
        ),
        migrations.AlterField(
            model_name='person',
            name='firstname',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='First name'),
        ),
        migrations.AlterField(
            model_name='person',
            name='fullname',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Full name'),
        ),
        migrations.AlterField(
            model_name='person',
            name='lastname',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Last name'),
        ),
        migrations.AlterField(
            model_name='person',
            name='location',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Location'),
        ),
    ]
