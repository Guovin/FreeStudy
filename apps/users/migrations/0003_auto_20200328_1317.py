# Generated by Django 2.2 on 2020-03-28 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200323_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='mobile',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='手机号码'),
        ),
    ]