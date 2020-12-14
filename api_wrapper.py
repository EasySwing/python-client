import requests


class APIWrapper:
    def __init__(self, Config):
        self.base_url = Config.base_url
        self.api_key = Config.api_key
        self.headers = {'Authorization': 'Bearer ' + self.api_key}

    def sign_in(self, tag_uuid):
        r = requests.get(self.base_url + '/sign_in/' + tag_uuid, headers=self.headers)
        try:
            return r.json()
        except:
            return None

