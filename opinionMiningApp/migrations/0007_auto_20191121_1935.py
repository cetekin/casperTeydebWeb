# Generated by Django 2.2.7 on 2019-11-21 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opinionMiningApp', '0006_comment_devicename'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='companyName',
            field=models.TextField(default='Casper'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='opinionminingresult',
            name='companyName',
            field=models.TextField(default='Casper'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='companyName',
            field=models.TextField(default='Casper'),
            preserve_default=False,
        ),
    ]
