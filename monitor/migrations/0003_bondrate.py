# Generated by Django 3.1.14 on 2023-04-29 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0002_commodityprice_stockprice'),
    ]

    operations = [
        migrations.CreateModel(
            name='BondRate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('bond_name', models.CharField(max_length=255)),
                ('annual_interest_rate', models.FloatField()),
                ('change_interest_rate', models.FloatField()),
                ('change_interest_rateByRate', models.FloatField()),
                ('updated_at', models.DateTimeField()),
            ],
        ),
    ]