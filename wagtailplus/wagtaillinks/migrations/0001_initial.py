# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers
import wagtail.wagtailadmin.taggable


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('link_type', models.PositiveIntegerField(verbose_name='Link Type', blank=True)),
                ('title', models.CharField(help_text='Enter a title for this link', max_length=100, verbose_name='Title')),
                ('email', models.EmailField(help_text='Enter a valid email address', max_length=254, verbose_name='Email', blank=True)),
                ('external_url', models.URLField(help_text='Enter a valid URL, including scheme (e.g. http://)', verbose_name='URL', blank=True)),
                ('tags', taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', blank=True, help_text=None, verbose_name='Tags')),
            ],
            options={
                'ordering': ('title',),
                'abstract': False,
                'verbose_name': 'Link',
                'verbose_name_plural': 'Links',
            },
            bases=(models.Model, wagtail.wagtailadmin.taggable.TagSearchable),
        ),
        migrations.CreateModel(
            name='EmailLink',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('wagtaillinks.link',),
        ),
        migrations.CreateModel(
            name='ExternalLink',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('wagtaillinks.link',),
        ),
    ]
