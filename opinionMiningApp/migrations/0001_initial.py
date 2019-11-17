# Generated by Django 2.2.7 on 2019-11-16 20:31

from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OpinionMiningResults',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('aspectStats', models.TextField()),
                ('deviceName', models.TextField()),
                ('beginDate', models.DateTimeField()),
                ('endDate', models.DateTimeField()),
                ('textCount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Texts',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('content', models.TextField()),
                ('testerName', models.TextField()),
                ('testDate', models.DateTimeField()),
                ('sentenceCount', models.IntegerField()),
                ('wordCount', models.IntegerField()),
                ('positiveWordCnt', models.IntegerField()),
                ('negativeWordCnt', models.IntegerField()),
            ],
        ),
    ]
