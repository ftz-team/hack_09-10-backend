# Generated by Django 3.2.8 on 2021-10-10 04:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_dataset_analytics'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dataset',
            name='analytics',
        ),
    ]