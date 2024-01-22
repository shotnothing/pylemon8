import requests
import random
import pprint
import functools 
import json

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
    
    def user(self, userId):
        '''Returns a User object of the specified userId.
        Args:
            userId (str): The id of the user.
        '''
        return User(self, userId)

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

class User:
    def __init__(self, lemon8, userId):
        '''Initialize a User object.
        Args:
            lemon8 (Lemon8): The Lemon8 session to use.
            userId (str): The id of the user.
        '''
        self.lemon8 = lemon8
        self.userId = userId
    
    def get_forced(self):
        '''Returns a requests.Response object of the user's profile page. This method is not cached. It is reccomended to use get() instead for the caching.'''
        url = f'https://www.lemon8-app.com/{self.userId}?region={self.lemon8.region}&position=follow_list&_data=routes%2F%24user_link_name&_version=1'
        response = self.lemon8.session.get(url)
        return response
    
    @functools.lru_cache(maxsize=16)
    def get(self):
        '''Returns a requests.Response object of the user's profile page. This method is cached.'''
        return self.get_forced()
    
    def get_profile_page(self, use_cached=True):
        '''Returns a tuple of the user's profile page and the user's details.
        Args:
            use_cached (bool): Whether to use the cached version of the profile page. Defaults to True.
        '''
        if not use_cached:
            return self.get_forced().text.split('\n')
        return self.get().text.split('\n')
    
    def get_details(self, use_cached=True):
        '''Returns a dict of the user's details.
        Args:
            use_cached (bool): Whether to use the cached version of the profile page. Defaults to True.
        '''
        return json.loads(self.get_profile_page(use_cached=use_cached)[0])[f'$UserDetailV2+{self.userId}']
    

pprint.pprint(Lemon8().user('bibipew').get_details(), indent=1)
