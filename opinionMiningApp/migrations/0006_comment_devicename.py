# Generated by Django 2.2.7 on 2019-11-20 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opinionMiningApp', '0005_auto_20191120_1640'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='deviceName',
            field=models.TextField(default='tempName'),
            preserve_default=False,
        ),
    ]