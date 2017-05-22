# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-22 11:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_id', models.CharField(blank=True, max_length=255, null=True)),
                ('main_title', models.CharField(blank=True, max_length=255, null=True)),
                ('sub_title', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Layout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, unique=True)),
                ('text_block', models.TextField(blank=True, max_length=5000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SmallContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, unique=True)),
                ('text_block', models.TextField(blank=True, max_length=5000, null=True)),
                ('icon', models.CharField(blank=True, max_length=255, null=True)),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.Content')),
            ],
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_title', models.CharField(max_length=255, unique=True)),
                ('sub_title', models.CharField(blank=True, max_length=255, null=True)),
                ('icon1', models.CharField(blank=True, default='fa fa-facebook', max_length=255, null=True)),
                ('url1', models.URLField(blank=True, max_length=255, null=True)),
                ('icon2', models.CharField(blank=True, default='fa fa-twitter', max_length=255, null=True)),
                ('url2', models.URLField(blank=True, max_length=255, null=True)),
                ('icon3', models.CharField(blank=True, default='fa fa-linkedin', max_length=255, null=True)),
                ('url3', models.URLField(blank=True, max_length=255, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='team')),
            ],
        ),
    ]