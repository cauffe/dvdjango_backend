# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('genre', models.CharField(max_length=255, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, null=True, blank=True)),
                ('status', models.CharField(max_length=255, null=True, blank=True)),
                ('price', models.CharField(max_length=255, null=True, blank=True)),
                ('rating', models.CharField(max_length=255, null=True, blank=True)),
                ('release', models.DateTimeField(null=True, blank=True)),
                ('genre', models.ForeignKey(blank=True, to='main.Genre', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Studio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('studio', models.CharField(max_length=255, null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='studio',
            field=models.ForeignKey(blank=True, to='main.Studio', null=True),
        ),
    ]
