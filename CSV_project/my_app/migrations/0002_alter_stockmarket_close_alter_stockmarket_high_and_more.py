# Generated by Django 4.1.3 on 2022-12-06 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockmarket',
            name='close',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='stockmarket',
            name='high',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='stockmarket',
            name='low',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='stockmarket',
            name='open',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='stockmarket',
            name='volume',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
