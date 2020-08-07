# Generated by Django 2.2 on 2020-03-23 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0001_initial'),
        ('operations', '0003_remove_coursecomments_is_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursecomments',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='organizations.Teacher', verbose_name='讲师'),
        ),
    ]