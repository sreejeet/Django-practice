# Generated by Django 2.0.5 on 2018-07-10 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoApp', '0002_itemtodo_time_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemtodo',
            name='time_added',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
