# Generated by Django 3.2.12 on 2023-12-01 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_alter_listing_buyer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='highest_bid',
            field=models.FloatField(default=models.FloatField()),
        ),
    ]
