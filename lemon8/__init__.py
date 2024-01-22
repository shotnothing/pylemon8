import requests
import random
import pprint

class Lemon8:
    def __init__(self, region='sg', cookie=None):
        self.region = region
        self.cookie = str(cookie) if cookie is not None else self._generate_tt_webid()
        self.session = requests.Session()
        self.session.headers.update({ 
            'cookie': f'tt_webid={self.cookie};',
            'user-agent': 'lemon8/1.0.0', # TODO: randomize
        })

    def feed(self, category):
        return Feed(self, category)
    
    def _generate_tt_webid(self):
        return ''.join(random.choice('0123456789') for i in range(19)) + '1'

class Feed:
    def __init__(self, lemon8, category = 'foryou'):
        self.lemon8 = lemon8
        self.category = category

    def get(self):
        url = f'https://www.lemon8-app.com/feed/{self.category}?method=stream-loadmore&_data=routes%2Ffeed.%24category_name&region={self.lemon8.region}&_version=1'
        response = self.lemon8.session.get(url)
        return response
    
    def get_json(self):
        return self.get().json()
    
    def get_items(self):
        key = f'$FeedDateLoadmore+{self.category}'
        return self.get_json()[key]['items'] 
    
    def pformat(self):
        return pprint.pformat(self.get_items(), indent=1)




