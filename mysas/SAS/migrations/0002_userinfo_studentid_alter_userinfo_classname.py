# Generated by Django 4.1.3 on 2022-11-22 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SAS', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='studentID',
            field=models.CharField(default='000', max_length=32),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='classname',
            field=models.CharField(default='ELC', max_length=32),
        ),
    ]