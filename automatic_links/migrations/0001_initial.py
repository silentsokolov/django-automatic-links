# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AutomaticLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keyword', models.CharField(unique=True, max_length=255, verbose_name='keyword')),
                ('link', models.CharField(max_length=255, verbose_name='link')),
                ('active', models.BooleanField(default=True, verbose_name='active')),
                ('limit', models.IntegerField(default=0, help_text='zero - disabled', verbose_name='limit')),
                ('every', models.IntegerField(default=1, help_text='Every "3" mean that this keyword will be replaced to link in every third content item', verbose_name='every N')),
                ('target', models.CharField(default=b'_blank', max_length=10, verbose_name='target', choices=[(b'_blank', b'_blank'), (b'_self', b'_self'), (b'_parent', b'_parent'), (b'_top', b'_top')])),
                ('nofollow', models.BooleanField(default=False, verbose_name='rel="nofollow"')),
                ('css_class', models.CharField(default=None, max_length=100, null=True, verbose_name='css class', blank=True)),
            ],
            options={
                'verbose_name': 'automatic link',
                'verbose_name_plural': 'automatic links',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='automaticlink',
            unique_together=set([('keyword', 'link')]),
        ),
    ]
