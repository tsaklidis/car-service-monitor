# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-08 15:33
from __future__ import unicode_literals

import datetime
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
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True)),
                ('website', models.URLField(help_text='Company website', verbose_name='Website')),
                ('founded', models.DateField(blank=True, default=datetime.date.today, help_text='When was company founded', null=True, verbose_name='Founded')),
                ('address', models.CharField(blank=True, help_text='Address', max_length=60, null=True)),
                ('city', models.CharField(blank=True, help_text='City', max_length=60, null=True)),
                ('company_size', models.IntegerField(default=0, help_text='How many employees does company have', verbose_name='Company Size')),
                ('manager', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['id'],
                'verbose_name_plural': 'companies',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text="Please give a name to company's department", max_length=100, verbose_name='Name')),
                ('slug', models.SlugField(blank=True, max_length=200, unique=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departments', to='companies.Company')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='department',
            unique_together=set([('company', 'name')]),
        ),
    ]
