
test_identity = { 
            'user_id' : 123, 
            'user' : {}, 
            'client_id' : 1111, 
            'client': {},
            'roles' : [],
            'privileges' : [],
            'api_key' : 'oh so secret api key'
            }

def add_user_context_to_request(event):
    settings = event.request.registry.settings
    req = event.request
    headers = req.headers
    client_id = headers.get('client_id',None)
    user_id = headers.get('user_id',None)
    api_key = headers.get('api_key',None)
    
    identity = {}
    
    if client_id and user_id and api_key:
        if validate(client,user_id,api_key):
            identity['client_id'] = client_id
            identity['user_id'] = user_id
            identity['api_key'] = api_key
    elif not settings.get('test_user_identity',None):
        identity = test_identity
        print 'User Test Identity'
    event.request['user_identity'] = identity
    print identity
    pass
    
def validate(client_id,user_id,api_key):
    return True
