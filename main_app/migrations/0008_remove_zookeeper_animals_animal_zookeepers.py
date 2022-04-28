# Generated by Django 4.0.4 on 2022-04-27 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_zookeeper_animals'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zookeeper',
            name='animals',
        ),
        migrations.AddField(
            model_name='animal',
            name='zookeepers',
            field=models.ManyToManyField(to='main_app.zookeeper'),
        ),
    ]
