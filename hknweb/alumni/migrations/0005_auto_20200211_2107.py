# Generated by Django 2.2.8 on 2020-02-12 05:07

import django.core.validators
from django.db import migrations, models
import hknweb.alumni.models


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0004_auto_20191003_2358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumnus',
            name='grad_year',
            field=models.IntegerField(default=2020, validators=[django.core.validators.MinValueValidator(1915), hknweb.alumni.models.max_value_current_year], verbose_name='graduation year'),
        ),
    ]
