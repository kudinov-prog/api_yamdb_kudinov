# Generated by Django 3.0.5 on 2020-08-28 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_user_confirmation_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='confirmation_code',
            field=models.CharField(default='FOOBAR', max_length=10),
        ),
    ]
