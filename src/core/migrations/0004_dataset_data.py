# Generated by Django 3.2.8 on 2021-10-09 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20211009_1925'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataset',
            name='data',
            field=models.FileField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
