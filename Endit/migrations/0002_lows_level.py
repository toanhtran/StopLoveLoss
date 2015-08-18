# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Endit', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lows',
            name='level',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
