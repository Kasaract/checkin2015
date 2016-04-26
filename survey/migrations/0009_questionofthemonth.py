# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0008_auto_20160124_1941'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionOfTheMonth',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.CharField(max_length=400, null=True, verbose_name=b'QuestionOfTheMonth:', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
