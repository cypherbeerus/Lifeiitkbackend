# Generated by Django 2.2.1 on 2019-07-02 16:21

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20190702_1027'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventmodel',
            name='hash_tags',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=40), blank=True, default=list, size=None),
        ),
    ]
