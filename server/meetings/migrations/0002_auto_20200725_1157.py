# Generated by Django 3.0.8 on 2020-07-25 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetings',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
