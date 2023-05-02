from django.test import TestCase
from investpy import get_stock_recent_data
from pandas.core.frame import DataFrame

class InvestpyTestCase(TestCase):
    def test_get_stock_recent_data(self):
        df = get_stock_recent_data('7974', 'japan')
        self.assertIsInstance(df, DataFrame)