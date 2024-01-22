import requests
import random
import pprint

class Lemon8:
    def __init__(self, region='sg', cookie=None):
        '''Initialize a Lemon8 session.
        Args:
            region (str): The region to use, as a two-letter code. Defaults to 'sg'.
            cookie (str): The tt_webid cookie to use. If not specified, a random one will be generated.
        '''
        self.region = region
        self.cookie = str(cookie) if cookie is not None else self._generate_tt_webid()
        self.session = requests.Session()
        self.session.headers.update({ 
            'cookie': f'tt_webid={self.cookie};',
            'user-agent': 'lemon8/1.0.0', # TODO: randomize
        })

    def feed(self, category):
        '''Returns a Feed object of the specified cateogry.
        Args:  
            category (str): The category to get. Known categories include: 'foryou', 'fashion', 'food', 'lifestyle', 'beauty'.
        '''
        return Feed(self, category)
    
    def _generate_tt_webid(self):
        '''Generates a random tt_webid cookie.'''
        return ''.join(random.choice('0123456789') for i in range(19)) + '1'

class Feed:
    def __init__(self, lemon8, category = 'foryou'):
        '''Initialize a Feed object.
        Args:
            lemon8 (Lemon8): The Lemon8 session to use.
            category (str): The category to get. Known categories include: 'foryou', 'fashion', 'food', 'lifestyle', 'beauty'. Defaults to 'foryou'.
        '''
        self.lemon8 = lemon8
        self.category = category

    def get(self):
        '''Returns a requests.Response object of the feed.'''
        url = f'https://www.lemon8-app.com/feed/{self.category}?method=stream-loadmore&_data=routes%2Ffeed.%24category_name&region={self.lemon8.region}&_version=1'
        response = self.lemon8.session.get(url)
        return response
    
    def get_dict(self):
        '''Returns a dict of the feed.'''
        return self.get().json()
    
    def get_items(self):
        '''Returns a list of dicts, corresponding to items in the feed.'''
        key = f'$FeedDateLoadmore+{self.category}'
        return self.get_dict()[key]['items'] 
    
    def pformat(self, indent=1):
        '''Returns a pretty-printed string of the feed.
        Args:
            indent (int): The indentation level to use. Defaults to 1.
        '''
        return pprint.pformat(self.get_items(), indent)




