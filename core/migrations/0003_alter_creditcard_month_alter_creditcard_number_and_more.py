# Generated by Django 4.0.4 on 2023-09-30 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_transaction_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditcard',
            name='month',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='number',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='year',
            field=models.CharField(max_length=4),
        ),
    ]
