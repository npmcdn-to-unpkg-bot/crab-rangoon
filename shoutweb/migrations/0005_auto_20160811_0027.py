# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-11 00:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
        ('shoutweb', '0004_auto_20160712_2223'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shouter',
            fields=[
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('modify_date', models.DateTimeField(auto_now=True)),
                ('avatar', models.CharField(blank=True, max_length=200, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='shouter', serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='users', to='shoutweb.Shouter'),
        ),
    ]