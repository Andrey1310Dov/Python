import requests

# PATH_TRADES = "trades.do"
# symbol = ltc_btc, etc_btc
# type = 1min/3min/5min/15min/30min/1day/1week/1hour/2hour/4hour/6hour/12hour

class BaseClient(object):
    def __init__(self, endpoint, path):
        self.endpoint = endpoint
        self.path = path


class OkexBaseClient(BaseClient):
    
    def __init__(self, endpoint, path):
        super().__init__(endpoint, path)

    def _get_parameters(self, value_symbol, value_type):
        parameters = {
            "symbol": value_symbol,
            "type": value_type,
        }
        return parameters
    
    def _build_parameters(self, parameters):
        keys = list(parameters.keys())
        keys.sort()
        params_for_request = '&'.join(["%s=%s" % (k, parameters[k]) for k in keys])
        return params_for_request

    def request(self):
        responce = requests.get(okex.endpoint + okex.path + '?' + params_for_request)
        return print(responce.text)

# okex = OkexBaseClient('https://www.okex.com/api/v1/', 'trades.do')
# parameters = okex._get_parameters('etc_btc', '1hour')
# params_for_request = okex._build_parameters(parameters)
# okex.request()
