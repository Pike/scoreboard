# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-13 12:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.TextField()),
                ('identifier', models.TextField()),
                ('original', models.TextField()),
                ('before', models.TextField()),
                ('after', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Locale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=30, unique=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MQMType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mqmid', models.CharField(db_index=True, max_length=50)),
                ('classification', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='mqm_base.Issue')),
                ('mqm_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mqm_base.MQMType')),
                ('rater', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='issue',
            name='locale',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='issues', to='mqm_base.Locale'),
        ),
    ]
