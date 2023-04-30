from djongo import models


class ExchangeRate(models.Model):  # usd/yen,canad/yen, gen/yen, euro/yen, ind/yen
    timestamp = models.DateTimeField()
    currency_pair = models.CharField(max_length=255)
    price = models.FloatField()
    change_price = models.FloatField()
    change_rate = models.FloatField()
    updated_at = models.DateTimeField()


class StockPrice(models.Model):  # nikkeiaverage, topix, nydau, nasdaq, s&p500
    timestamp = models.DateTimeField()
    index_name = models.CharField(max_length=255)
    price = models.FloatField()
    change_price = models.FloatField()
    change_rate = models.FloatField()
    updated_at = models.DateTimeField()


class CommodityPrice(models.Model):  # wticrude, gold, platina, silver
    timestamp = models.DateTimeField()
    commodity_name = models.CharField(max_length=255)
    price = models.FloatField()
    change_price = models.FloatField()
    change_rate = models.FloatField()
    updated_at = models.DateTimeField()

class BondRate(models.Model):  # 国債
    timestamp = models.DateTimeField()
    bond_name = models.CharField(max_length=255)
    annual_interest_rate = models.FloatField()
    change_interest_rate = models.FloatField()
    change_interest_rateByRate = models.FloatField()
    updated_at = models.DateTimeField()


class FedRate(models.Model):
    timestamp = models.DateTimeField()
    fed_name = models.CharField(max_length=255)
    fedRate = models.FloatField()
    change_fedRate = models.FloatField()
    change_fedRateByRate = models.FloatField()
    updated_at = models.DateTimeField()


class ShippingIndex(models.Model):  # バルチック、定期船運賃
    timestamp = models.DateTimeField()
    index_name = models.CharField(max_length=255)
    index_value = models.FloatField()
    change_price = models.FloatField()
    change_rate = models.FloatField()
    updated_at = models.DateTimeField()


class GdpData(models.Model):  # GDP
    timestamp = models.DateTimeField()
    country_name = models.CharField(max_length=255)
    gdp = models.FloatField()
    change_gdp = models.FloatField()
    change_rate = models.FloatField()
    updated_at = models.DateTimeField()


class News(models.Model):
    timestamp = models.DateTimeField()
    title = models.CharField(max_length=255)
    content = models.TextField()
    published_at = models.DateTimeField()
