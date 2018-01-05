# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20180105_0259'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todo',
            options={'ordering': ('is_completed', '-update_at')},
        ),
        migrations.RenameField(
            model_name='todo',
            old_name='created_at',
            new_name='create_at',
        ),
        migrations.RenameField(
            model_name='todo',
            old_name='completed',
            new_name='is_completed',
        ),
        migrations.RenameField(
            model_name='todo',
            old_name='updated_at',
            new_name='update_at',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='description',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='title',
        ),
        migrations.AddField(
            model_name='todo',
            name='content',
            field=models.TextField(default=datetime.datetime(2018, 1, 5, 3, 25, 33, 459870, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='todo',
            name='id',
            field=models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True),
        ),
    ]
