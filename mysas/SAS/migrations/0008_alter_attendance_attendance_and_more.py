# Generated by Django 4.1.3 on 2022-11-26 05:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SAS', '0007_remove_attendance_attendancepercentage_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='attendance',
            field=models.CharField(max_length=16, verbose_name='attendance'),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='classname',
            field=models.CharField(max_length=32, verbose_name='classname'),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='date',
            field=models.DateField(verbose_name='date'),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='grade',
            field=models.IntegerField(verbose_name='grade'),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='starttime',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(9), django.core.validators.MaxValueValidator(17)], verbose_name='startTime'),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='studentID',
            field=models.CharField(max_length=32, verbose_name='studentID'),
        ),
    ]