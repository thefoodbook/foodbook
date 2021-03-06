# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodbook', '0003_auto_20160117_0138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_dislikes',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='image_likes',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='image_tags',
            field=models.CommaSeparatedIntegerField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='image_text',
            field=models.CharField(max_length=140, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='image_url',
            field=models.CharField(max_length=600, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='image_views',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='restaurant_key',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='favorite_restaurants',
            field=models.CommaSeparatedIntegerField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='image_tags',
            field=models.CommaSeparatedIntegerField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='user_profile_name',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
