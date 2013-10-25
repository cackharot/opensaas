from ..library.http_helpers import get_url
import simplejson as json

base_url = "http://127.0.0.1:6543/users"
user_id = 123
api_key = "oh so secret key"

class UserProxy(object):
    """ User REST Proxy """
    def __init__(self):
        pass
        
    def get_users(self,client_id):
        data = None #{'client_id':client_id}
        code,headers,resp = get_url(base_url,data=data,client_id=client_id,user_id=user_id,api_key=api_key)
        
        if code == 200 and resp:
            users = json.loads(resp)
            return users
        return None
        
    def get_user(self,user_id,client_id):
        return None
        
    def create_user(self,user,client_id):
        code,headers,resp = get_url(base_url,method='PUT',
                data=user,
                client_id=client_id,
                user_id=user_id,
                api_key=api_key)
        
        if code == 200 and resp:
            result = json.loads(resp)
            return result
