import pkgutil
from typing import List

from dataclass_csv import DataclassReader

from kabu.model import Company


class TSE:
    def __init__(self) -> None:
        data = pkgutil.get_data(__name__, 'data/stocks.csv')
        if data:
            reader = DataclassReader(data.decode('utf-8').splitlines(), Company)
        else:
            raise Exception('File not found.')

        self.companies: List[Company] = [row for row in reader]

    def get_all(self):
        return self.companies

    def get_topix_core30(self):
        return [x for x in self.companies if x.topix_new_index_series_code == 1]

    def get_topix_large70(self):
        return [x for x in self.companies if x.topix_new_index_series_code == 2]

    def get_topix_100(self):
        return self.get_topix_core30() + self.get_topix_large70()

    def get_topix_mid400(self):
        return [x for x in self.companies if x.topix_new_index_series_code == 4]

    def get_topix_500(self):
        return self.get_topix_100() + self.get_topix_mid400()

    def get_topix_small_1(self):
        return [x for x in self.companies if x.topix_new_index_series_code == 6]

    def get_topix_small_2(self):
        return [x for x in self.companies if x.topix_new_index_series_code == 7]

    def get_topix_1000(self):
        return self.get_topix_500() + self.get_topix_small_1()

    def get_nikkei225(self):
        return [x for x in self.companies if x.nikkei225]