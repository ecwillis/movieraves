# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moviedb', '0002_auto_20150125_0740'),
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('slug', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('actor', models.ForeignKey(to='moviedb.Actor')),
                ('movie', models.ForeignKey(to='moviedb.Movie')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
