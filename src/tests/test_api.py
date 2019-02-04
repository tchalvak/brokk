import requests
import json
#import pprint
#import config

API_BASE = 'https://t8wwrnycz5.execute-api.us-east-1.amazonaws.com/dev/' # Move this to config later

class TestApi:
    ''' Hits the api endpoints and checks for json coming back
    '''

    def root(self):
        '''Get the root url from the config'''
        return API_BASE

    def status_code(self, url):
        ''' Gets http status codes of the urls '''
        try:
            r = requests.head(url, verify=False)
            return r.status_code
        except requests.ConnectionError:
            return None

    def pull_json(self, url, endpoint):
        ''' Get a page to parse as json, for the api '''
        params = dict(
            type=endpoint,
            jsoncallback='fake'
            )
        resp = requests.get(url=url, params=params, verify=False)
        cut = resp.text
        return cut


    def test_root_url_config_works(self):
        ''' Ensure root is configured '''
        assert (self.root() is not None and
                len(str(self.root())) > 5)


    def test_api_urls(self):
        endpoints = ['register', 'order', 'subscribe', 'payment-method/card', 'payment-method/bank-account', 
            'payment-method/source', 'initiate-payment-intent', 'payments', 'search-transactions', 
            'query', 'mutate']
        player_data = self.pull_json(self.root(), 'register') 
        assert (player_data is not None)
        for endpoint in endpoints:
            data = self.pull_json(self.root(), endpoint)
            assert (data is not None and 
                json.loads(data) is not False and
                len(json.loads(data)) > 0
            )

