# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConfirmString',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('code', models.CharField(max_length=256)),
                ('c_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': '确认码',
                'ordering': ['-c_time'],
                'verbose_name': '确认码',
            },
        ),
        migrations.AddField(
            model_name='user',
            name='has_confirmed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='confirmstring',
            name='user',
            field=models.OneToOneField(to='login.User'),
        ),
    ]
