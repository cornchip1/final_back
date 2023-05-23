# Generated by Django 3.2.18 on 2023-05-23 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('en_name', models.CharField(max_length=300)),
                ('filmos', models.TextField()),
                ('img', models.TextField(default='')),
            ],
        ),
    ]