# Generated by Django 2.2.7 on 2019-11-17 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opinionMiningApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='opinionminingresults',
            name='beginDate',
        ),
        migrations.RemoveField(
            model_name='opinionminingresults',
            name='endDate',
        ),
        migrations.AddField(
            model_name='opinionminingresults',
            name='reportDate',
            field=models.TextField(default='noDate'),
        ),
    ]
