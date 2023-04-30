# Generated by Django 3.1.14 on 2023-04-29 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0003_bondrate'),
    ]

    operations = [
        migrations.CreateModel(
            name='FedRate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('fed_name', models.CharField(max_length=255)),
                ('fedRate', models.FloatField()),
                ('change_fedRate', models.FloatField()),
                ('change_fedRateByRate', models.FloatField()),
                ('updated_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='GdpData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('country_name', models.CharField(max_length=255)),
                ('gdp', models.FloatField()),
                ('change_gdp', models.FloatField()),
                ('change_rate', models.FloatField()),
                ('updated_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('published_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='ShippingIndex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('index_name', models.CharField(max_length=255)),
                ('index_value', models.FloatField()),
                ('change_price', models.FloatField()),
                ('change_rate', models.FloatField()),
                ('updated_at', models.DateTimeField()),
            ],
        ),
    ]
