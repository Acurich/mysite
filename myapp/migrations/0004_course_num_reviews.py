# Generated by Django 3.1.2 on 2020-11-24 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20201006_1041'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='num_reviews',
            field=models.PositiveIntegerField(default=0),
        ),
    ]