# Generated by Django 2.1.2 on 2018-10-19 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='finished_at',
            field=models.DateTimeField(null=True),
        ),
    ]
