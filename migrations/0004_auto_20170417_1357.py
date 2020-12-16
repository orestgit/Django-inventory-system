# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_auto_20170417_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='bucket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, null=True, to='inventory.Bucket'),
        ),
        migrations.AlterField(
            model_name='item',
            name='desc',
            field=models.TextField(blank=True),
        ),
    ]
