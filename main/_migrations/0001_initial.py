# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, null=True, blank=True)),
                ('studio', models.CharField(max_length=255, null=True, blank=True)),
                ('status', models.CharField(max_length=255, null=True, blank=True)),
                ('genre', models.CharField(max_length=255, null=True, blank=True)),
                ('release', models.DateTimeField(null=True, blank=True)),
            ],
        ),
    ]
