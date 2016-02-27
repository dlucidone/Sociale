# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('full_name', models.CharField(max_length=120, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.CharField(max_length=1000, null=True)),
            ],
        ),
    ]
