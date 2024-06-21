# Generated by Django 5.0.6 on 2024-06-20 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AvailabilityDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('is_available', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'AvailabilityDate',
            },
        ),
        migrations.CreateModel(
            name='ETF',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('etf_name', models.CharField(max_length=100)),
                ('etf_shortname', models.CharField(max_length=30)),
                ('etf_link', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'ETF',
            },
        ),
        migrations.CreateModel(
            name='ETF_holdings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=255)),
                ('sector', models.CharField(max_length=100)),
                ('asset_class', models.CharField(max_length=100)),
                ('market_value', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('weight', models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True)),
                ('notional_value', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('shares', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
                ('exchange', models.CharField(blank=True, max_length=100, null=True)),
                ('currency', models.CharField(blank=True, max_length=10, null=True)),
                ('fx_rate', models.DecimalField(blank=True, decimal_places=6, max_digits=10, null=True)),
                ('market_currency', models.CharField(blank=True, max_length=10, null=True)),
                ('accrual_date', models.DateField(blank=True, null=True)),
                ('etfname', models.CharField(blank=True, max_length=255, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('firm', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'ETF_holdings',
            },
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_name', models.CharField(max_length=100)),
                ('stock_shortname', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Stock',
            },
        ),
    ]
