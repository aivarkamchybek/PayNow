# Generated by Django 4.0.4 on 2023-08-30 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_kyc'),
    ]

    operations = [
        migrations.AddField(
            model_name='kyc',
            name='identity_image',
            field=models.ImageField(blank=True, null=True, upload_to='kyc'),
        ),
    ]