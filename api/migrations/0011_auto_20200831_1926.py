# Generated by Django 3.0.5 on 2020-08-31 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_title_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='genre',
            name='title',
        ),
        migrations.AddField(
            model_name='title',
            name='genre',
            field=models.ManyToManyField(to='api.Genre'),
        ),
        migrations.AddField(
            model_name='title',
            name='rating',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='title',
            name='description',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='title',
            name='year',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
