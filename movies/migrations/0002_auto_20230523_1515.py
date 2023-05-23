# Generated by Django 3.2.18 on 2023-05-23 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='casts',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='directors',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='genre_ids',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='overview',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='poster_path',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='release_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='vote_average',
            field=models.FloatField(null=True),
        ),
    ]