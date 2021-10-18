import settings
import requests
from exceptions import APICallError

class StockTimeSeries:
    def __init__(self):
        self.base_url = settings.BASE_URL
        self.api_key = settings.APIKEY

    def _build_url(self, path):
        return f"{self.base_url}?{path}&apikey={self.api_key}"


    def _api_request(self, url):
        resp = requests.get(url)

        if resp.status_code == 200:
            return print(resp.json())
        else:
            raise APICallError(
            f"Não foi possível consumir o serviço: STATUS_CODE"
            f"={resp.status_code}"
        )

    def _url_treatment(self, function, symbol, *interval, **kwargs):
        path = f'function={function}&symbol={symbol}&interval={"".join(interval)}'
        options = [f'{item[0]}={item[1]}' for item in kwargs.items()]
        path = f"{path}&{'&'.join(options)}" if options else path
        return path

    def intraday_series(self, function, symbol, interval, **kwargs):
        path = self._url_treatment(function, symbol, interval, **kwargs) #cria o path
        url = self._build_url(path) #realiza a construção da url completa

        resp = self._api_request(url) #faz um get na api e retorna um .json

    def daily_series(self, function, symbol, **kwargs):
        path = self._url_treatment(function, symbol, **kwargs)
        url = self._build_url(path)

        resp = self._api_request(url)

    def weekly_series(self, function, symbol, **kwargs):
        path = self._url_treatment(function, symbol, **kwargs)
        url = self._build_url(path)

        resp = self._api_request(url)
                

    def monthly_series(self, function, symbol, **kwargs):
        path = self._url_treatment(function, symbol, **kwargs)    
        url = self._build_url(path)

        resp = self._api_request(url)