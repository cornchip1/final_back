# Generated by Django 3.2.18 on 2023-05-23 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('today', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='img',
            field=models.TextField(default='', null=True),
        ),
    ]
