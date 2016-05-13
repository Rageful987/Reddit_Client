import requests
import json
import credentials


class reddit_client(object):
    def __init__(self):
        user_pass_dict = {
                        'user': credentials.reddit['user'],
                        'passwd': credentials.reddit['passw'],
                        'api_type': 'json'}

        headers = {'user-agent': '/u/Beneaths\'s API python bot'}

        self.client = requests.session()
        self.client.headers = headers
        r = self.client.post(r'http://www.reddit.com/api/login',
                             data=user_pass_dict)
        j = json.loads(r.content)
        self.client.modhash = j['json']['data']['modhash']

    def get_frontpage(self):
        '''sends a request to reddit.com'''

        data = self.client.get(r'http://www.reddit.com/.json')

        return self.json_to_dict(data)

    def json_to_dict(self, data):
        j = json.loads(data.content)

        if j['data']['children']:
            return j['data']['children']
        else:
            return None

    def get_user_data(self, username):
        '''gets information on the provided username.'''

        data = self.client.get(
                        r'http://www.reddit.com/u/{0}/.json'.format(username))

        return self.json_to_dict(data)
