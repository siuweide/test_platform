# Generated by Django 3.1.3 on 2021-05-16 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_manage', '0002_auto_20210322_1515'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='module',
            options={'ordering': ('-create_time',)},
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ('-create_time',)},
        ),
    ]
