# Generated by Django 5.0.6 on 2024-06-22 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ETF_services', '0002_delete_availabilitydate_etf_etf_stocks_etf_stocks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='stock_name',
            field=models.CharField(max_length=500),
        ),
    ]
